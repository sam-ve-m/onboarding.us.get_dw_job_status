from unittest.mock import patch

from etria_logger import Gladsheim
from flask import Flask
from pytest import mark
from werkzeug.test import Headers

from main import get_employment_status_enum
from src.services.employment_status.service import EmploymentStatusService

get_employment_status_enum_result_dummy = [
    {"code": "EMPLOYED", "value": "EMPREGADO(A)"}
]


@mark.asyncio
@patch.object(EmploymentStatusService, "get_employment_status_enum")
async def test_get_employment_status_enum_when_request_is_ok(onboarding_steps_mock):
    onboarding_steps_mock.return_value = get_employment_status_enum_result_dummy

    app = Flask(__name__)
    with app.test_request_context(
        headers=Headers({"x-thebes-answer": "test"}),
    ).request as request:

        get_employment_status_enum_result = await get_employment_status_enum(request)

    assert (
        get_employment_status_enum_result.data
        == b'{"result": [{"code": "EMPLOYED", "value": "EMPREGADO(A)"}], "message": "Success", "success": true, "code": 0}'
    )
    assert onboarding_steps_mock.called


@mark.asyncio
@patch.object(Gladsheim, "error")
@patch.object(EmploymentStatusService, "get_employment_status_enum")
async def test_get_employment_status_enum_when_generic_exception_happens(
    onboarding_steps_mock, etria_mock
):
    onboarding_steps_mock.side_effect = Exception("erro")

    app = Flask(__name__)
    with app.test_request_context(
        headers=Headers({"x-thebes-answer": "test"}),
    ).request as request:

        get_employment_status_enum_result = await get_employment_status_enum(request)

    assert (
        get_employment_status_enum_result.data
        == b'{"result": null, "message": "Unexpected error occurred", "success": false, "code": 100}'
    )
    assert onboarding_steps_mock.called
    etria_mock.assert_called()

from unittest.mock import patch

from etria_logger import Gladsheim
from flask import Flask
from heimdall_client.bifrost import Heimdall
from heimdall_client.bifrost import HeimdallStatusResponses
from pytest import mark
from werkzeug.test import Headers

from main import get_enums
from src.service.employ_status_enum.service import EmployStatusEnumService

decoded_jwt_ok = {
    "is_payload_decoded": True,
    "decoded_jwt": {"user": {"unique_id": "test"}},
    "message": "Jwt decoded",
}
decoded_jwt_invalid = {
    "is_payload_decoded": False,
    "decoded_jwt": {"user": {"unique_id": "test_error"}},
    "message": "Jwt decoded",
}

service_response_dummy = '{"result": [{"code": "AGRICULTURE", "value": "AGRICULTURE"}, {"code": "EMPLOYED", "value": "EMPLOYED"}, {"code": "RETIRED", "value": "RETIRED"}], "message": null, "success": true, "code": 0}'


@mark.asyncio
@patch.object(EmployStatusEnumService, "get_response")
@patch.object(Heimdall, "decode_payload")
async def test_get_enums_when_request_is_ok(decode_payload_mock, get_response_mock):
    decode_payload_mock.return_value = (decoded_jwt_ok, HeimdallStatusResponses.SUCCESS)
    get_response_mock.return_value = service_response_dummy

    app = Flask(__name__)
    with app.test_request_context(
        headers=Headers({"x-thebes-answer": "test"}),
    ).request as request:

        get_enums_result = await get_enums(request)

        assert (
            get_enums_result.data
            == b'{"result": [{"code": "AGRICULTURE", "value": "AGRICULTURE"}, {"code": "EMPLOYED", "value": "EMPLOYED"}, {"code": "RETIRED", "value": "RETIRED"}], "message": null, "success": true, "code": 0}'
        )
        assert get_response_mock.called
        decode_payload_mock.assert_called_with(jwt="test")


@mark.asyncio
@patch.object(Gladsheim, "error")
@patch.object(EmployStatusEnumService, "get_response")
@patch.object(Heimdall, "decode_payload")
async def test_get_enums_when_jwt_is_invalid(
    decode_payload_mock, get_response_mock, etria_mock
):
    decode_payload_mock.return_value = (
        decoded_jwt_invalid,
        HeimdallStatusResponses.INVALID_TOKEN,
    )
    get_response_mock.return_value = True

    app = Flask(__name__)
    with app.test_request_context(
        headers=Headers({"x-thebes-answer": "test_error"}),
    ).request as request:

        get_enums_result = await get_enums(request)

        assert (
            get_enums_result.data
            == b'{"result": [], "message": "JWT invalid or not supplied", "success": false, "code": 30}'
        )
        assert not get_response_mock.called
        decode_payload_mock.assert_called_with(jwt="test_error")
        etria_mock.assert_called()


@mark.asyncio
@patch.object(Gladsheim, "error")
@patch.object(EmployStatusEnumService, "get_response")
@patch.object(Heimdall, "decode_payload")
async def test_get_enums_when_type_error_happens(
    decode_payload_mock, get_response_mock, etria_mock
):
    decode_payload_mock.return_value = (decoded_jwt_ok, HeimdallStatusResponses.SUCCESS)
    get_response_mock.side_effect = TypeError("erro")

    app = Flask(__name__)
    with app.test_request_context(
        headers=Headers({"x-thebes-answer": "test"}),
    ).request as request:

        get_enums_result = await get_enums(request)

        assert (
            get_enums_result.data
            == b'{"result": [], "message": "Data not found or inconsistent.", "success": false, "code": 99}'
        )
        assert get_response_mock.called
        decode_payload_mock.assert_called_with(jwt="test")
        etria_mock.assert_called()


@mark.asyncio
@patch.object(Gladsheim, "error")
@patch.object(EmployStatusEnumService, "get_response")
@patch.object(Heimdall, "decode_payload")
async def test_get_enums_when_generic_exception_happens(
    decode_payload_mock, get_response_mock, etria_mock
):
    decode_payload_mock.return_value = (decoded_jwt_ok, HeimdallStatusResponses.SUCCESS)
    get_response_mock.side_effect = Exception("erro")

    app = Flask(__name__)
    with app.test_request_context(
        headers=Headers({"x-thebes-answer": "test"}),
    ).request as request:

        get_enums_result = await get_enums(request)

        assert (
            get_enums_result.data
            == b'{"result": [], "message": "Error trying to get the enum.", "success": false, "code": 100}'
        )
        assert get_response_mock.called
        decode_payload_mock.assert_called_with(jwt="test")
        etria_mock.assert_called()

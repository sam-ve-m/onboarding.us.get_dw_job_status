from http import HTTPStatus

from etria_logger import Gladsheim
from flask import request, Response, Request

from src.domain.exceptions.model import UnauthorizedError
from src.domain.response.model import ResponseModel
from src.domain.jwt.model import Jwt
from src.domain.response.status_code.enums import StatusCode
from src.service.gender_enum.service import GenderEnumService


async def get_enums(request_: Request = request) -> Response:
    try:
        x_thebes_answer = request_.headers.get("x-thebes-answer")
        await Jwt.validate_jwt(x_thebes_answer)

        service_response = GenderEnumService.get_response()
        response = ResponseModel.build_http_response(
            response_model=service_response, status=HTTPStatus.OK
        )
        return response

    except UnauthorizedError as error:
        message = "JWT invalid or not supplied"
        Gladsheim.error(error=error, message=message)
        response = ResponseModel.build_http_response(
            response_model=ResponseModel.build_response(
                success=False,
                code=StatusCode.JWT_INVALID,
                message=message,
                result=[],
            ),
            status=HTTPStatus.NOT_FOUND,
        )
        return response

    except TypeError as error:
        message = "Data not found or inconsistent."
        Gladsheim.error(error=error, message=message)
        response = ResponseModel.build_http_response(
            response_model=ResponseModel.build_response(
                success=False,
                code=StatusCode.DATA_NOT_FOUND,
                message="Data not found or inconsistent.",
                result=[],
            ),
            status=HTTPStatus.NOT_FOUND,
        )
        return response

    except Exception as error:
        message = "Error trying to get the enum."
        Gladsheim.error(error=error, message=message)
        response = ResponseModel.build_http_response(
            response_model=ResponseModel.build_response(
                success=False,
                code=StatusCode.INTERNAL_SERVER_ERROR,
                message="Error trying to get the enum.",
                result=[],
            ),
            status=HTTPStatus.INTERNAL_SERVER_ERROR,
        )
        return response

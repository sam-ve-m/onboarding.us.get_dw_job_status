from src.core.interfaces.service.employ_status_enum.interface import (
    IEmployStatusEnumService,
)
from src.domain.response.model import ResponseModel
from src.domain.response.status_code.enums import StatusCode
from src.repository.employ_status_enum.repository import EmployStatusEnumRepository


class EmployStatusEnumService(IEmployStatusEnumService):
    @classmethod
    def get_response(cls):
        service_response = []

        enums = EmployStatusEnumRepository.get_employ_status_enum()
        for code, value in enums:
            service_response.append({"code": code, "value": value})

        service_response = ResponseModel.build_response(
            success=True, code=StatusCode.SUCCESS, message=None, result=service_response
        )
        return service_response

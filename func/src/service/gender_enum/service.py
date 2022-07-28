from src.core.interfaces.service.gender_enum.interface import IGenderEnumService
from src.domain.response.model import ResponseModel
from src.domain.response.status_code.enums import StatusCode
from src.repository.gender_enum.repository import GenderEnumRepository


class GenderEnumService(IGenderEnumService):
    @classmethod
    def get_response(cls):
        service_response = []

        enums = GenderEnumRepository.get_gender_enum()
        for code, value in enums:
            service_response.append({"code": code, "value": value})

        service_response = ResponseModel.build_response(
            success=True, code=StatusCode.SUCCESS, message=None, result=service_response
        )
        return service_response

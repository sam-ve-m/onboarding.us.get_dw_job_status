from heimdall_client import Heimdall, HeimdallStatusResponses

from src.domain.exceptions.model import UnauthorizedError


class Jwt:
    @classmethod
    async def validate_jwt(cls, jwt: str):
        jwt_content, heimdall_status = await Heimdall.decode_payload(jwt=jwt)
        if heimdall_status != HeimdallStatusResponses.SUCCESS:
            raise UnauthorizedError

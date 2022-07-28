import asyncio
from heimdall_client import Heimdall, HeimdallStatusResponses

from src.domain.exceptions.model import UnauthorizedError


class Jwt:
    __event_loop = asyncio.get_event_loop()

    @classmethod
    def validate_jwt(cls, jwt: str):
        decode_jwt_coroutine = Heimdall.decode_payload(jwt=jwt)
        jwt_content, heimdall_status = cls.__event_loop.run_until_complete(decode_jwt_coroutine)
        # jwt_content, heimdall_status = await Heimdall.decode_payload(jwt=jwt)
        if heimdall_status != HeimdallStatusResponses.SUCCESS:
            raise UnauthorizedError

    # @classmethod
    # def get_loop(cls):
    #     if cls.__event_loop is None:
    #         cls.__event_loop = asyncio.get_event_loop()
    #     return cls.__event_loop

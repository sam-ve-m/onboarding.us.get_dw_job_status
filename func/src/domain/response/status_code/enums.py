from enum import IntEnum


class StatusCode(IntEnum):
    SUCCESS = 0
    INVALID_PARAMS = 10
    DATA_NOT_FOUND = 99
    JWT_INVALID = 30
    INTERNAL_SERVER_ERROR = 100

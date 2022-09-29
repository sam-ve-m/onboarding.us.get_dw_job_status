from typing import Union

from etria_logger import Gladsheim
from mnemosine import SyncCache

from src.core.interfaces.repository.enum_employ_status_cache.interface import (
    IEnumEmployStatusCacheRepository,
)


class EnumEmployStatusCacheRepository(IEnumEmployStatusCacheRepository):
    enum_key = "jormungandr:EnumEmployStatus"

    @classmethod
    def save_enum_employ_status(cls, enum: list, time: int = 3600) -> bool:
        try:
            SyncCache.save(cls.enum_key, list(enum), int(time))
            return True
        except ValueError as error:
            Gladsheim.error(error=error, message="Error saving enum in cache.")
            return False
        except TypeError as error:
            Gladsheim.error(error=error, message="Error saving enum in cache.")
            return False
        except Exception as error:
            Gladsheim.error(error=error, message="Error saving enum in cache.")
            return False

    @classmethod
    def get_enum_employ_status(cls) -> Union[list, None]:
        result = None
        try:
            result = SyncCache.get(cls.enum_key)
        except Exception as error:
            Gladsheim.error(error=error, message="Error getting enum in cache.")
        return result

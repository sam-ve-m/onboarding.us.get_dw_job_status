from typing import List, Tuple

from src.core.interfaces.repository.employ_status_enum.interface import (
    IEmployStatusEnumRepository,
)
from src.repository.enum_employ_status_cache.repository import (
    EnumEmployStatusCacheRepository,
)
from src.repository.base_repository.oracle.repository import OracleBaseRepository


class EmployStatusEnumRepository(IEmployStatusEnumRepository):

    enum_query = """
            SELECT CODE as code, DESCRIPTION as description
            FROM USPIXDB001.SINCAD_EXTERNAL_EMPLOY_STATUS
        """

    @classmethod
    def get_employ_status_enum(cls) -> List[Tuple]:
        sql = cls.enum_query
        result = cls._get_employ_status_cached_enum(sql)
        return result

    @classmethod
    def _get_employ_status_cached_enum(cls, query: str) -> List[Tuple]:
        if cached_enum := EnumEmployStatusCacheRepository.get_enum_employ_status():
            return cached_enum

        enum_values = OracleBaseRepository.query(sql=query)
        EnumEmployStatusCacheRepository.save_enum_employ_status(enum_values)
        return enum_values

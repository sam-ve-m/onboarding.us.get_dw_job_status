from abc import ABC, abstractmethod
from typing import List, Any


class IEmployStatusEnumRepository(ABC):
    @abstractmethod
    def get_employ_status_enum(self) -> List[Any]:
        pass

    @abstractmethod
    def _get_employ_status_cached_enum(self, query: str) -> List[Any]:
        pass

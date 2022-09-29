from abc import ABC, abstractmethod
from typing import Any


class IEnumEmployStatusCacheRepository(ABC):
    @abstractmethod
    def save_enum_employ_status(self, enum: Any, time: int):
        pass

    @abstractmethod
    def get_enum_employ_status(self) -> Any:
        pass

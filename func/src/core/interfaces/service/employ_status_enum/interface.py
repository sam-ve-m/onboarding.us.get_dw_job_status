from abc import ABC, abstractmethod


class IEmployStatusEnumService(ABC):
    @abstractmethod
    def get_response(self):
        pass

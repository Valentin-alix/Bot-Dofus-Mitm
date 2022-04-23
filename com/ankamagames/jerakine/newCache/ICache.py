from abc import ABC
from typing import Any


class ICache(ABC):
    @property
    def size(self) -> int:
        pass

    def destroy(self) -> None:
        pass

    def contains(self, param1) -> bool:
        pass

    def extract(self, param1) -> Any:
        pass

    def peek(self, param1) -> Any:
        pass

    def store(self, param1, param2) -> bool:
        pass

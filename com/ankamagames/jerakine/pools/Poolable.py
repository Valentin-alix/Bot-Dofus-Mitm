from abc import ABC


class Poolable(ABC):
    def free(self) -> None:
        pass

from abc import ABC


class CancelableMessage(ABC):
    @property
    def cancel(self) -> bool:
        pass

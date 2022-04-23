from threading import Timer
from typing import Any


class SoftReference:
    def __init__(self, obj, keptTime: int = 10):
        self.value = obj
        self.keptTime = keptTime
        self.timeout = None
        self.resetTimeout()

    @property
    def object(self) -> Any:
        self.resetTimeout()
        return self.value

    def resetTimeout(self) -> None:
        if self.timeout:
            self.timeout.cancel()
        if self.value:
            self.timeout = Timer(self.keptTime, self.clearReference)
            self.timeout.start()

    def clearReference(self) -> None:
        del self.value
        self.value = None

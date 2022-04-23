from types import FunctionType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.jerakine.network.messages.Worker import Worker
from com.ankamagames.jerakine.messages.Treatment import Treatment


class ForeachTreatment(Treatment):

    _iterator: int = 0

    _worker: "Worker"

    def __init__(
        self, obj, func: FunctionType, params: list, iterable, worker: "Worker"
    ):
        self.params = []
        self.params.insert(0, None)
        super().__init__(obj, func, params)
        self._iterable = iterable
        self._worker = worker

    def process(self) -> bool:
        if len(self._iterable) == 0:
            return True
        self.params[0] = self._iterable[self._iterator]
        self._iterator += 1
        self.calledfunction(self.object, self.params)
        return len(self._iterable) <= self._iterator

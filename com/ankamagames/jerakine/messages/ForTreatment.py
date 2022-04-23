from types import FunctionType
from com.ankamagames.jerakine.network.messages import Worker
from com.ankamagames.jerakine.messages.Treatment import Treatment


class ForTreatment(Treatment):
    def __init__(
        self, object, func: FunctionType, params: list, iterations: int, worker: Worker
    ):
        params.insert(0, None)
        super().__init__(object, func, params)
        self._iterations: int = 0
        self._maxIterations = iterations
        self._worker = worker

    def process(self) -> bool:
        self.params[0] = self._iterations
        self.calledfunction(self.object, self.params)
        self._iterations += 1
        return self._iterations >= self._maxIterations

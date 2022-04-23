from types import FunctionType
from time import perf_counter
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.jerakine.network.messages.Worker import Worker
logger = Logger(__name__)


class EnterFrameDispatcher(metaclass=Singleton):
    def __init__(self):
        self._maxAllowedTime: int = 20
        self._listenerUp: bool = False
        self._workerListenerUp: bool = False
        self._currentTime: int = perf_counter()
        self._postWorkerTime: int = 0
        self._diff: int = 0
        self._noWorkerFrameCount: int = 0
        self._controledListeners = dict[FunctionType, ControledEnterFrameListener]()
        self._worker: "Worker" = None

    def addWorker(self, w: "Worker") -> None:
        self._worker = w
        self.handleEnterFrameEvents()
        self.handleWorkers()

    def removeWorker(self) -> None:
        if self._workerListenerUp:
            self._workerListenerUp = False

    @property
    def enterFrameListenerCount(self) -> int:
        return len(self._controledListeners)

    @property
    def controledEnterFrameListeners(self) -> dict:
        return self._controledListeners

    @property
    def worker(self) -> "Worker":
        return self._worker

    def addEventListener(
        self, listener: FunctionType, name: str, frameRate: int = 0.004294967295e9
    ) -> None:
        if not self._controledListeners.get(listener):
            exp1 = 0 if frameRate == float("inf") else int(1 / frameRate)
            self._controledListeners[listener] = ControledEnterFrameListener(
                name,
                listener,
                frameRate <= 0 or exp1,
                int(self._currentTime) if not self._listenerUp else int(perf_counter()),
            )
            if not self._listenerUp:
                self._listenerUp = True

    def hasEventListener(self, listener: FunctionType) -> bool:
        return self._controledListeners.get(listener) != None

    @property
    def maxAllowedTime(self) -> int:
        return self._maxAllowedTime

    @maxAllowedTime.setter
    def maxAllowedTime(self, time: int) -> None:
        self._maxAllowedTime = time

    def removeEventListener(self, listener: FunctionType) -> None:
        if self._controledListeners.get(listener):
            del self._controledListeners[listener]
            if len(self._controledListeners) == 0 and not self._workerListenerUp:
                self._listenerUp = False

    def handleEnterFrameEvents(self) -> None:
        self._currentTime = perf_counter()
        try:
            for cefl in self._controledListeners.values():
                diff = self._currentTime - cefl.latestChange
                if diff > cefl.wantedGap - cefl.overhead:
                    cefl.listener()
                    cefl.latestChange = self._currentTime
                    cefl.overhead = diff - cefl.wantedGap + cefl.overhead
        except RuntimeError:
            pass

    def remainsTime(self) -> bool:
        return perf_counter() - self._postWorkerTime < self._maxAllowedTime

    def handleWorkers(self) -> None:
        _diff = perf_counter() - self._postWorkerTime
        if _diff < self._maxAllowedTime:
            self._worker.processQueues(self._maxAllowedTime - _diff)
            self._noWorkerFrameCount = 0
        else:
            self._worker.processQueues(self._noWorkerFrameCount)
            if self._noWorkerFrameCount < self._maxAllowedTime / 2:
                self._noWorkerFrameCount += 1
        self._postWorkerTime = perf_counter()


class ControledEnterFrameListener:
    name: str
    listener: FunctionType
    wantedGap: int
    overhead: int
    latestChange: int

    def __init__(
        self, name: str, listener: FunctionType, wantedGap: int, latestChange: int
    ):
        self.name = name
        self.listener = listener
        self.wantedGap = wantedGap
        self.latestChange = latestChange
        self.overhead = 0

from time import perf_counter
from com.ankamagames.dofus.logic.common.utils.Lagometer import Lagometer
from com.ankamagames.dofus.network.messages.game.basic.BasicAckMessage import (
    BasicAckMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.ILagometer import ILagometer
from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage

logger = Logger(__name__)


class LagometerAck(Lagometer):

    _msgTimeStack: list[int]

    _active: bool = False

    _optionId: int

    def __init__(self):
        self._msgTimeStack = list[int]()
        super().__init__()

    def stop(self) -> None:
        if self._timer.is_alive():
            self._timer.cancel()
        self._msgTimeStack = []

    def ping(self, msg: INetworkMessage = None) -> None:
        if not self._active:
            super().ping(msg)
            return
        if not len(self._msgTimeStack):
            self._timer = self.SHOW_LAG_DELAY
            self._timer.start()
        self._msgTimeStack.append(perf_counter())

    def pong(self, msg: INetworkMessage = None) -> None:
        latency: int = 0
        if not self._active:
            super().pong(msg)
            return
        if isinstance(msg, BasicAckMessage):
            latency = perf_counter() - self._msgTimeStack.pop(0)
            if latency > self.SHOW_LAG_DELAY:
                logger.debug(latency + " ms de latence (bas� sur ACK)")
                self.startLag()
                self._timer.cancel()
            else:
                self.stopLag()
                if len(self._msgTimeStack):
                    self._timer.delay = max(
                        0,
                        self.SHOW_LAG_DELAY - (perf_counter() - self._msgTimeStack[0]),
                    )
                    self._timer.start()
                else:
                    self._timer.cancel()

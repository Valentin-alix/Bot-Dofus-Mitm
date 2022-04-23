from threading import Event
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.utils.display.EnterFrameConst import EnterFrameConst
import com.ankamagames.jerakine.utils.display.EnterFrameDispatcher as efd


class FrameIdManager(metaclass=Singleton):
    def __init__(self):
        self._init: bool = False
        self._frameId: int = 0
        efd.EnterFrameDispatcher().addEventListener(
            self.onEnterFrame, EnterFrameConst.FRAME_ID_MANAGER
        )

    @property
    def frameId(self) -> int:
        return self._frameId

    def onEnterFrame(self) -> None:
        self._frameId += 1

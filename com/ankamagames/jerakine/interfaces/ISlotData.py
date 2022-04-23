from com.ankamagames.jerakine.interfaces.ISlotDataHolder import ISlotDataHolder


class ISlotData:
    @property
    def info1(self) -> str:
        pass

    @property
    def active(self) -> bool:
        pass

    @property
    def timer(self) -> int:
        pass

    @property
    def startTime(self) -> int:
        pass

    @property
    def endTime(self) -> int:
        pass

    @endTime.setter
    def endTime(self, param1: int) -> None:
        pass

    def addHolder(self, param1: ISlotDataHolder) -> None:
        pass

    def removeHolder(self, param1: ISlotDataHolder) -> None:
        pass

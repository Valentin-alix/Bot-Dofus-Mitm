from com.ankamagames.jerakine.interfaces.ISlotData import ISlotData
from com.ankamagames.jerakine.interfaces.ISlotDataHolder import ISlotDataHolder
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class SlotDataHolderManager:

    _weakHolderReference: dict

    _linkedSlotsData: list[ISlotData]

    def __init__(self, linkedSlotData: ISlotData):
        self._weakHolderReference = dict()
        super().__init__()
        self._linkedSlotsData = list[ISlotData]()
        self._linkedSlotsData.append(linkedSlotData)

    def setLinkedSlotData(self, slotData: ISlotData) -> None:
        if not self._linkedSlotsData:
            self._linkedSlotsData = list[ISlotData]()
        if slotData not in self._linkedSlotsData:
            self._linkedSlotsData.append(slotData)

    def addHolder(self, h: ISlotDataHolder) -> None:
        self._weakHolderReference[h] = True

    def removeHolder(self, h: ISlotDataHolder) -> None:
        del self._weakHolderReference[h]

    def getHolders(self) -> list:
        return list(self._weakHolderReference.keys())

    def refreshAll(self) -> None:
        for h in self._weakHolderReference:
            for linkedSlotData in self._linkedSlotsData:
                if h and ISlotDataHolder(h).data == linkedSlotData:
                    h.refresh()

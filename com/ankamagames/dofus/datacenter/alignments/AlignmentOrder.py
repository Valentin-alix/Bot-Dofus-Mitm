from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.dofus.types.IdAccessors import IdAccessors


class AlignmentOrder:
    MODULE = "AlignmentOrder"

    id: int

    nameId: int

    sideId: int

    @classmethod
    def getAlignmentOrders(cls) -> list["AlignmentOrder"]:
        return GameData.getObjects(cls.MODULE)

    @classmethod
    def getAlignmentOrderById(cls, id) -> "AlignmentOrder":
        return GameData.getObject(cls.MODULE, id)

    idAccessors = IdAccessors(getAlignmentOrderById, getAlignmentOrders)

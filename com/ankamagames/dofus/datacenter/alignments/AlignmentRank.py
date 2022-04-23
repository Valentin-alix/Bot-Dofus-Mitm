from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.dofus.types.IdAccessors import IdAccessors


class AlignmentRank:
    MODULE = "AlignmentRank"

    id: int

    orderId: int

    nameId: int

    descriptionId: int

    minimumAlignment: int

    gifts: list[int]

    @classmethod
    def getAlignmentRanks(cls) -> list["AlignmentRank"]:
        return GameData.getObjects(cls.MODULE)

    @classmethod
    def getAlignmentRankById(cls, id) -> "AlignmentRank":
        return GameData.getObject(cls.MODULE, id)

    idAccessors = IdAccessors(getAlignmentRankById, getAlignmentRanks)

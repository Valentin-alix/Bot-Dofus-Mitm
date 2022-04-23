from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.dofus.types.IdAccessors import IdAccessors


class AlignmentRankJntGift:
    MODULE = "AlignmentRankJntGift"

    id: int

    gifts: list[int]

    levels: list[int]

    @classmethod
    def getAlignmentRankJntGifts(cls) -> list["AlignmentRankJntGift"]:
        return GameData.getObjects(cls.MODULE)

    @classmethod
    def getAlignmentRankJntGiftById(cls, id) -> "AlignmentRankJntGift":
        return GameData.getObject(cls.MODULE, id)

    idAccessors = IdAccessors(getAlignmentRankJntGiftById, getAlignmentRankJntGifts)

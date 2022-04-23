from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.dofus.types.IdAccessors import IdAccessors


class AlignmentGift:
    MODULE = "AlignmentGift"

    id: int

    nameId: int

    @classmethod
    def getAlignmentGifts(cls) -> list["AlignmentGift"]:
        return GameData.getObjects(cls.MODULE)

    @classmethod
    def getAlignmentGiftById(cls, id) -> "AlignmentGift":
        return GameData.getObject(cls.MODULE, id)

    idAccessors = IdAccessors(getAlignmentGiftById, getAlignmentGifts)

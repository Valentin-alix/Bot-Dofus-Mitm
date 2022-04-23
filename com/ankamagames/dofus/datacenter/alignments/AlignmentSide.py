from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.dofus.types.IdAccessors import IdAccessors


class AlignmentSide:
    MODULE = "AlignmentSides"

    id: int

    nameId: int

    @classmethod
    def getAlignmentSides(cls) -> list["AlignmentSide"]:
        return GameData.getObjects(cls.MODULE)

    @classmethod
    def getAlignmentSideById(cls, id) -> "AlignmentSide":
        return GameData.getObject(cls.MODULE, id)

    idAccessors = IdAccessors(getAlignmentSideById, getAlignmentSides)

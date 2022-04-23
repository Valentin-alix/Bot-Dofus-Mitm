from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class Incarnation(IDataCenter):

    MODULE: str = "Incarnation"

    _incarnationsList: list

    id: int

    maleBoneId: int

    femaleBoneId: int

    lookMale: str

    lookFemale: str

    def __init__(self):
        super().__init__()

    @classmethod
    def getIncarnationById(cls, id: int) -> "Incarnation":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getAllIncarnation(cls) -> list:
        if not cls._incarnationsList:
            cls._incarnationsList = GameData.getObjects(cls.MODULE)
        return cls._incarnationsList

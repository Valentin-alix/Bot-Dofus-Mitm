from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class PresetIcon(IDataCenter):

    MODULE: str = "PresetIcons"

    id: int

    order: int

    def __init__(self):
        super().__init__()

    @classmethod
    def getPresetIconById(cls, id: int) -> "PresetIcon":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getPresetIcons(cls) -> list:
        return GameData.getObjects(cls.MODULE)

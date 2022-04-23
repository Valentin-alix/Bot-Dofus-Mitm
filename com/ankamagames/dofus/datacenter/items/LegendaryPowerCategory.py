from logging import Logger
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class LegendaryPowerCategory(IDataCenter):

    MODULE: str = "LegendaryPowersCategories"

    logger = Logger(__name__)

    id: int

    categoryName: str

    categoryOverridable: bool

    categorySpells: list[int]

    def __init__(self):
        super().__init__()

    def getLegendaryPowerCategoryById(cls, id: int) -> "LegendaryPowerCategory":
        return GameData.getObject(cls.MODULE, id)

    def getLegendaryPowersCategories(cls) -> list:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(
        getLegendaryPowerCategoryById, getLegendaryPowersCategories
    )

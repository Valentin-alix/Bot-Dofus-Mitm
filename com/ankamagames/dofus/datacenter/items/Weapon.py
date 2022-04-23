from com.ankamagames.dofus.datacenter.items.Item import Item
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class Weapon(Item, IDataCenter):

    apCost: int

    minRange: int

    range: int

    maxCastPerTurn: int

    castInLine: bool

    castInDiagonal: bool

    castTestLos: bool

    criticalHitProbability: int

    criticalHitBonus: int

    criticalFailureProbability: int

    def __init__(self):
        super().__init__()

    def getWeaponById(self, weaponId: int) -> "Weapon":
        item: Item = Item.getItemById(weaponId)
        if item and item.isWeapon:
            return Weapon(item)
        return None

    def getWeapons(self) -> list:
        item: Item = None
        items: list = Item.getItems()
        result: list = list()
        for item in items:
            if item.isWeapon:
                result.append(item)
        return result

    idAccessors = IdAccessors(getWeaponById, getWeapons)

    @property
    def isWeapon(self) -> bool:
        return True

    def copy(self, src: Item, to: Item) -> None:
        super().copy(src, to)
        if to.hasOwnProperty("apCost") and src.hasOwnProperty("apCost"):
            to.apCost = src.apCost
            to.minRange = src.minRange
            to.range = src.range
            to.maxCastPerTurn = src.maxCastPerTurn
            to.castInLine = src.castInLine
            to.castInDiagonal = src.castInDiagonal
            to.castTestLos = src.castTestLos
            to.criticalHitProbability = src.criticalHitProbability
            to.criticalHitBonus = src.criticalHitBonus
            to.criticalFailureProbability = src.criticalFailureProbability
        else:
            logger.error(
                "Failed to properly copy weapon data " + src.id + " to " + to.id
            )

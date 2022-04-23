from com.ankamagames.dofus.datacenter.items.Weapon import Weapon
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper


class WeaponWrapper(ItemWrapper):

    _weaponUtil: Weapon = Weapon()

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

    @property
    def isWeapon(self) -> bool:
        return True

    @classmethod
    def clone(cls, baseobject: object = None) -> ItemWrapper:
        result: ItemWrapper = super().clone(WeaponWrapper)
        cls._weaponUtil.copy(cls, result)
        return result

from com.ankamagames.jerakine.data import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.dofus.types.IdAccessors import IdAccessors


class SpellState(IDataCenter):
    MODULE: str = "SpellStates"

    id: int

    nameId: int

    preventsSpellCast: bool

    preventsFight: bool

    isSilent: bool

    cantDealDamage: bool

    invulnerable: bool

    incurable: bool

    cantBeMoved: bool

    cantBePushed: bool

    cantSwitchPosition: bool

    effectsIds: list[int]

    icon: str = ""

    iconVisibilityMask: int

    invulnerableMelee: bool

    invulnerableRange: bool

    cantTackle: bool

    cantBeTackled: bool

    displayTurnRemaining: bool

    @staticmethod
    def getSpellStateById(id: int):
        return GameData.getObject(SpellState.MODULE, id)

    @staticmethod
    def getSpellStates() -> list:
        return GameData.getObjects(SpellState.MODULE)

    idAccessors: IdAccessors = IdAccessors(getSpellStateById, getSpellStates)

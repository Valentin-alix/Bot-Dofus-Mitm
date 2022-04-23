from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.game.common.spell.SpellModifier import SpellModifier
from com.ankamagames.dofus.logic.game.fight.actions.UpdateSpellModifierAction import (
    UpdateSpellModifierAction,
)
import com.ankamagames.dofus.logic.game.fight.managers.SpellModifiersManager as spellmm
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class SpellModifiers:
    def __init__(self, entityId: float, spellId: float):
        super().__init__()
        self._entityId = entityId
        self._spellId = spellId
        self._modifiers = dict()

    @property
    def entityId(self) -> float:
        return self._entityId

    @property
    def spellId(self) -> float:
        return self._spellId

    @property
    def modifiers(self) -> dict:
        return self._modifiers

    @property
    def isVerbose(self) -> bool:
        return spellmm.SpellModifiersManager().isVerbose

    def getFormattedMessage(self, message: str) -> str:
        return (
            self.__class__.__name__
            + " (Entity ID: "
            + str(self._entityId)
            + ", Spell ID: "
            + str(self._spellId)
            + "): "
            + message
        )

    def setModifier(self, modifier: SpellModifier) -> None:
        modifier.entityId = self._entityId
        modifier.spellId = self._spellId
        self._modifiers[str(modifier.id)] = modifier
        if self.isVerbose:
            logger.info(
                "Set modifier for entity with ID "
                + str(self.entityId)
                + " and spell with ID "
                + str(self.spellId)
                + ": "
                + str(modifier)
            )
        updateSpellModifierAction = UpdateSpellModifierAction.create(
            self.entityId, self.spellId, modifier.id
        )
        Kernel.getWorker().process(updateSpellModifierAction)

    def getModifier(self, modifierId: float) -> SpellModifier:
        if modifierId not in self._modifiers:
            return None
        return self._modifiers[str(modifierId)]

    def deleteModifier(self, modifierId: float) -> None:
        if modifierId not in self._modifiers:
            return
        modifierKey: str = str(modifierId)
        modifier: SpellModifier = self._modifiers[modifierKey]
        if self.isVerbose:
            logger.info(
                "Deleted modifier for entity with ID "
                + str(self._entityId)
                + " and spell with ID "
                + str(self._spellId)
                + ": "
                + str(modifier)
            )
        del self._modifiers[modifierKey]

    def resetModifiers(self) -> None:
        if self.isVerbose:
            logger.info(
                "Modifiers reset for entity with ID "
                + str(self._entityId)
                + " and spell with ID "
                + str(self._spellId)
            )
        self._modifiers = dict()

    def getSpellModifiersNumber(self) -> float:
        return len(self._modifiers)

    def hasModifier(self, modifierId: float) -> bool:
        return str(modifierId) in self._modifiers

    def getModifierValue(self, modifierId: float) -> float:
        key: str = str(modifierId)
        if modifierId not in self._modifiers:
            return 0
        modifier: SpellModifier = self._modifiers.get(key)
        return float(modifier.totalValue) if modifier is not None else float(0)

    def getModifierBaseValue(self, modifierId: float) -> float:
        key: str = str(modifierId)
        if modifierId not in self._modifiers:
            return 0
        return self._modifiers[key].baseValue

    def getModifierContextModifValue(self, modifierId: float) -> float:
        key: str = str(modifierId)
        if modifierId not in self._modifiers:
            return 0
        return self._modifiers[key].contextModifValue

    def __str__(self) -> str:
        spellModifierId: float = None
        spellModifiersDump: str = ""
        spellModifierIds: list[float] = list[float]()
        spellModifier: SpellModifier = None
        for spellModifier in self._modifiers:
            spellModifierIds.append(spellModifier.id)
        spellModifierIds.sort()
        for spellModifierId in spellModifierIds:
            spellModifier = self._modifiers[str(spellModifierId)]
            spellModifiersDump += "\n\t" + str(spellModifier)
        if not spellModifiersDump:
            spellModifiersDump = "\n\tNo spell modifiers to display."
        return self.getFormattedMessage(spellModifiersDump)

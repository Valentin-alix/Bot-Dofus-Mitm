from com.ankamagames.dofus.datacenter.spells.Spell import Spell
from com.ankamagames.dofus.datacenter.spells.SpellLevel import SpellLevel
import com.ankamagames.dofus.internalDatacenter.spells.SpellWrapper as spellw
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.dofus.logic.game.fight.managers.SpellCastInFightManager import (
        SpellCastInFightManager,
    )
from com.ankamagames.dofus.network.enums.CharacterSpellModificationTypeEnum import (
    CharacterSpellModificationTypeEnum,
)
from com.ankamagames.jerakine.logger.Logger import Logger


class SpellManager:

    logger = Logger(__name__)

    _spellId: int

    _spellLevel: int

    _lastCastTurn: int

    _spellHasBeenCast: bool

    _forcedCooldown: bool

    _lastInitialCooldownReset: int

    _castThisTurn: int

    _targetsThisTurn: dict

    _spellCastManager: "SpellCastInFightManager"

    _castIntervalModificator: int

    _castIntervalSetModificator: int

    def __init__(
        self,
        spellCastManager: "SpellCastInFightManager",
        pSpellId: int,
        pSpellLevel: int,
    ):
        super().__init__()
        self._spellCastManager = spellCastManager
        self._spellId = pSpellId
        self._spellLevel = pSpellLevel
        self._targetsThisTurn = dict()

    def isForgettableSpell(self, spellId: int) -> bool:
        return ForgettableSpell.getForgettableSpellById(spellId) is not None

    @property
    def numberCastThisTurn(self) -> int:
        return self._castThisTurn

    @property
    def spellLevel(self) -> int:
        return self._spellLevel

    @spellLevel.setter
    def spellLevel(self, pSpellLevel: int) -> None:
        self._spellLevel = pSpellLevel

    @property
    def spell(self) -> Spell:
        return Spell.getSpellById(self._spellId)

    def cast(self, pTurn: int, pTarget: list, pCountForCooldown: bool = True) -> None:
        self._castIntervalModificator = self._castIntervalSetModificator = 0
        self._lastCastTurn = pTurn
        self._forcedCooldown = False
        self._spellHasBeenCast = True
        for target in pTarget:
            if self._targetsThisTurn[target] == None:
                self._targetsThisTurn[target] = 0
            self._targetsThisTurn[target] += 1
        if pCountForCooldown:
            self._castThisTurn += 1
        self.updateSpellWrapper()

    def resetInitialCooldown(self, pTurn: int) -> None:
        self._lastInitialCooldownReset = pTurn
        self.updateSpellWrapper()

    def getCastOnEntity(self, pEntityId: float) -> int:
        if self._targetsThisTurn[pEntityId] is None:
            return 0
        return self._targetsThisTurn[pEntityId]

    def newTurn(self) -> None:
        self._castThisTurn = 0
        self._targetsThisTurn = dict()
        self.updateSpellWrapper()

    @property
    def cooldown(self) -> float:
        interval: float = None
        cooldown: int = 0
        spell: Spell = Spell.getSpellById(self._spellId)
        spellLevel: SpellLevel = spell.getSpellLevel(self._spellLevel)
        spellModifiers = SpellModifiersManager().getSpellModifiers(
            self._spellCastManager.entityId, self._spellId
        )
        castIntervalModifier: float = 0
        castIntervalSetModifier: float = 0
        if spellModifiers is not None:
            castIntervalModifier = spellModifiers.getModifierValue(
                CharacterSpellModificationTypeEnum.CAST_INTERVAL
            )
            castIntervalSetModifier = spellModifiers.getModifierValue(
                CharacterSpellModificationTypeEnum.CAST_INTERVAL_SET
            )
        if castIntervalModifier:
            self._castIntervalModificator = castIntervalModifier
        else:
            castIntervalModifier = self._castIntervalModificator
        if castIntervalSetModifier:
            self._castIntervalSetModificator = castIntervalSetModifier
        else:
            castIntervalSetModifier = self._castIntervalSetModificator
        if castIntervalSetModifier:
            interval = -castIntervalModifier + castIntervalSetModifier
        else:
            interval = spellLevel.minCastInterval - (
                0 if castIntervalModifier < 0 else castIntervalModifier
            )
        if interval == 63:
            return 63
        initialCooldown: int = (
            self._lastInitialCooldownReset
            + spellLevel.initialCooldown
            - self._spellCastManager.currentTurn
        )
        if (
            self._lastCastTurn
            >= self._lastInitialCooldownReset + spellLevel.initialCooldown
            or spellLevel.initialCooldown == 0
            or self._forcedCooldown
            or self._castThisTurn > 0
            or self._spellHasBeenCast
        ):
            cooldown = (
                interval + self._lastCastTurn - self._spellCastManager.currentTurn
            )
        else:
            cooldown = initialCooldown
        if cooldown <= 0:
            cooldown = 0
        return cooldown

    def forceCooldown(self, cooldown: int, isBonusRefresh: bool = False) -> None:
        spell: Spell = Spell.getSpellById(self._spellId)
        spellL: SpellLevel = spell.getSpellLevel(self._spellLevel)
        self._lastCastTurn = (
            cooldown + self._spellCastManager.currentTurn - spellL.minCastInterval
        )
        self._forcedCooldown = True
        spellW: spellw.SpellWrapper = spellw.SpellWrapper.getSpellWrapperById(
            self._spellId, self._spellCastManager.entityId
        )
        if isBonusRefresh:
            cooldown -= self._castIntervalModificator
        spellW.actualCooldown = cooldown

    def forceLastCastTurn(self, pLastCastTurn: int) -> None:
        self._lastCastTurn = pLastCastTurn
        self._forcedCooldown = False
        self.updateSpellWrapper()

    def updateSpellWrapper(self) -> None:
        spellW: spellw.SpellWrapper = spellw.SpellWrapper.getSpellWrapperById(
            self._spellId, self._spellCastManager.entityId
        )
        if spellW == None:
            spellW = spellw.SpellWrapper.create(
                self._spellId, self._spellLevel, True, self._spellCastManager.entityId
            )
        if spellW and spellW.actualCooldown != 63:
            spellW.actualCooldown = self.cooldown

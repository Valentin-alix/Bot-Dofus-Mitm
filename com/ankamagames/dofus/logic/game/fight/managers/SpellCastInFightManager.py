from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.game.fight.types.castSpellManager.SpellManager import (
    SpellManager,
)
from com.ankamagames.dofus.network.enums.CharacterSpellModificationTypeEnum import (
    CharacterSpellModificationTypeEnum,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import (
    GameFightSpellCooldown,
)
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class SpellCastInFightManager:

    _spells: dict

    _storedSpellCooldowns: list[GameFightSpellCooldown]

    currentTurn: int = 1

    entityId: float

    needCooldownUpdate: bool = False

    def __init__(self, entityId: float):
        self._spells = dict()
        super().__init__()
        self.entityId = entityId

    def nextTurn(self) -> None:
        spell: SpellManager = None
        ++self.currentTurn
        for spell in self._spells:
            spell.newTurn()

    def resetInitialCooldown(self, hasBeenSummoned: bool = False) -> None:
        spim: SpellInventoryManagementFrame = Kernel.getWorker().getFrame(
            SpellInventoryManagementFrame
        )
        spellList: list = spim.getFullSpellListByOwnerId(self.entityId)
        for spellWrapper in spellList:
            if spellWrapper.spellLevelInfos.initialCooldown != 0:
                if (
                    hasBeenSummoned
                    and spellWrapper.actualCooldown
                    > spellWrapper.spellLevelInfos.initialCooldown
                ):
                    return
                if self._spells[spellWrapper.spellId] == None:
                    self._spells[spellWrapper.spellId] = SpellManager(
                        self, spellWrapper.spellId, spellWrapper.spellLevel
                    )
                spellManager = self._spells[spellWrapper.spellId]
                spellManager.resetInitialCooldown(self.currentTurn)

    def updateCooldowns(
        self, spellCooldowns: list[GameFightSpellCooldown] = None
    ) -> None:
        from com.ankamagames.dofus.internalDatacenter.spells.SpellWrapper import (
            SpellWrapper,
        )
        from com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import (
            CurrentPlayedFighterManager,
        )
        from com.ankamagames.dofus.logic.game.fight.managers.SpellModifiersManager import (
            SpellModifiersManager,
        )

        if self.needCooldownUpdate and not spellCooldowns:
            spellCooldowns = self._storedSpellCooldowns
        playedFighterManager: CurrentPlayedFighterManager = (
            CurrentPlayedFighterManager()
        )
        numCoolDown: int = len(spellCooldowns)
        for k in range(numCoolDown):
            spellCooldown = spellCooldowns[k]
            spellW = SpellWrapper.getSpellWrapperById(
                spellCooldown.spellId, self.entityId
            )
            if not spellW:
                self.needCooldownUpdate = True
                self._storedSpellCooldowns = spellCooldowns
                return
            if spellW and spellW.spellLevel > 0:
                spellLevel = spellW.spell.getSpellLevel(spellW.spellLevel)
                spellCastManager = playedFighterManager.getSpellCastManagerById(
                    self.entityId
                )
                spellCastManager.castSpell(spellW.id, spellW.spellLevel, [], False)
                interval = spellLevel.minCastInterval
                if spellCooldown.cooldown != 63:
                    castInterval = 0
                    castIntervalSet = 0
                    spellModifiers = SpellModifiersManager().getSpellModifiers(
                        self.entityId, spellW.id
                    )
                    if spellModifiers is not None:
                        castInterval = spellModifiers.getModifierValue(
                            CharacterSpellModificationTypeEnum.CAST_INTERVAL
                        )
                        castIntervalSet = spellModifiers.getModifierValue(
                            CharacterSpellModificationTypeEnum.CAST_INTERVAL_SET
                        )
                    if castIntervalSet:
                        interval = -castInterval + castIntervalSet
                    else:
                        interval -= castInterval
                spellCastManager.getSpellManagerBySpellId(spellW.id).forceLastCastTurn(
                    self.currentTurn + spellCooldown.cooldown - interval
                )
        self.needCooldownUpdate = False

    def castSpell(
        self,
        pSpellId: int,
        pSpellLevel: int,
        pTargets: list,
        pCountForCooldown: bool = True,
    ) -> None:
        if self._spells[pSpellId] == None:
            self._spells[pSpellId] = SpellManager(self, pSpellId, pSpellLevel)
        self._spells[pSpellId]

    def getSpellManagerBySpellId(
        self, pSpellId: int, isForceNewInstance: bool = False, pSpellLevelId: int = -1
    ) -> SpellManager:
        spellManager: SpellManager = self._spells[pSpellId]
        if spellManager == None and isForceNewInstance and pSpellLevelId != -1:
            spellManager = self._spells[pSpellId] = SpellManager(
                self, pSpellId, pSpellLevelId
            )
        return spellManager

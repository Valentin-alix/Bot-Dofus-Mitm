from operator import methodcaller
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDice import (
    EffectInstanceDice,
)
from com.ankamagames.dofus.datacenter.spells.Spell import Spell
from com.ankamagames.dofus.datacenter.spells.SpellLevel import SpellLevel
from com.ankamagames.dofus.internalDatacenter.spells.SpellWrapper import SpellWrapper
from com.ankamagames.dofus.kernel.Kernel import Kernel
import com.ankamagames.dofus.logic.game.fight.fightEvents.FightEventsHelper as fightEventsHelper
import com.ankamagames.dofus.logic.game.fight.frames.FightBattleFrame as fightBattleFrame
import com.ankamagames.dofus.logic.game.fight.frames.FightEntitiesFrame as fightEntitiesFrame
from com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import (
    CurrentPlayedFighterManager,
)
import com.ankamagames.dofus.logic.game.fight.types.BasicBuff as basicBuff
from com.ankamagames.dofus.logic.game.fight.types.CastingSpell import CastingSpell
from com.ankamagames.dofus.logic.game.fight.types.StatBuff import StatBuff
from com.ankamagames.dofus.misc.utils.GameDebugManager import GameDebugManager
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import (
    AbstractFightDispellableEffect,
)
from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import (
    FightTemporaryBoostEffect,
)
from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostStateEffect import (
    FightTemporaryBoostStateEffect,
)
from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostWeaponDamagesEffect import (
    FightTemporaryBoostWeaponDamagesEffect,
)
from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporarySpellBoostEffect import (
    FightTemporarySpellBoostEffect,
)
from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporarySpellImmunityEffect import (
    FightTemporarySpellImmunityEffect,
)
from com.ankamagames.dofus.network.types.game.actions.fight.FightTriggeredEffect import (
    FightTriggeredEffect,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import (
    GameFightFighterInformations,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton

logger = Logger(__name__)


class BuffManager(metaclass=Singleton):

    INCREMENT_MODE_SOURCE: int = 1

    INCREMENT_MODE_TARGET: int = 2

    _buffs: dict

    spellBuffsToIgnore: list[CastingSpell]

    def __init__(self):
        self._buffs = dict()
        self.spellBuffsToIgnore = list[CastingSpell]()
        super().__init__()

    def makeBuffFromEffect(
        self,
        effect: AbstractFightDispellableEffect,
        castingSpell: CastingSpell,
        actionId: int,
    ) -> basicBuff.BasicBuff:
        criticalEffect: bool = False
        if GameDebugManager().buffsDebugActivated:
            logger.debug("[BUFFS DEBUG] Creation du buff " + effect.uid)

        if isinstance(effect, FightTemporarySpellBoostEffect):
            buff = SpellBuffeffect
            if GameDebugManager().buffsDebugActivated:
                logger.debug(
                    "[BUFFS DEBUG]      Buff " + effect.uid + " : type SpellBuff"
                )

        if isinstance(effect, FightTriggeredEffect):
            buff = TriggeredBuffeffect
            if GameDebugManager().buffsDebugActivated:
                logger.debug(
                    "[BUFFS DEBUG]      Buff " + effect.uid + " : type TriggeredBuff"
                )

        if isinstance(effect, FightTemporaryBoostWeaponDamagesEffect):
            ftbwde = effect
            buff = basicBuff.BasicBuff(
                effect,
                castingSpell,
                actionId,
                ftbwde.weaponTypeId,
                ftbwde.delta,
                ftbwde.weaponTypeId,
            )
            if GameDebugManager().buffsDebugActivated:
                logger.debug(
                    "[BUFFS DEBUG]      Buff "
                    + str(effect.uid)
                    + " : type BasicBuff avec FightTemporaryBoostWeaponDamagesEffect"
                )

        if isinstance(effect, FightTemporaryBoostStateEffect):
            buff = StateBuffeffect
            if GameDebugManager().buffsDebugActivated:
                logger.debug(
                    "[BUFFS DEBUG]      Buff " + effect.uid + " : type StateBuff"
                )

        if isinstance(effect, FightTemporarySpellImmunityEffect):
            ftsie = effect
            buff = basicBuff.BasicBuff(
                effect, castingSpell, actionId, ftsie.immuneSpellId, None, None
            )
            if GameDebugManager().buffsDebugActivated:
                logger.debug(
                    "[BUFFS DEBUG]      Buff "
                    + effect.uid
                    + " : type BasicBuff avec FightTemporarySpellImmunityEffect"
                )

        if isinstance(effect, FightTemporaryBoostEffect):
            buff = StatBuffFactory.createStatBuffeffect
            if GameDebugManager().buffsDebugActivated:
                logger.debug(
                    "[BUFFS DEBUG]      Buff " + effect.uid + " : type StatBuff"
                )

        buff.id = effect.uid
        spellLevelsId: int = -1
        spell: Spell = Spell.getSpellById(effect.spellId)
        for level in spell.spellLevelsInfo:
            for effectInstanceDice in level.effects:
                if effectInstanceDice.effectUid == effect.effectId:
                    spellLevelsId = level.id
            if spellLevelsId == -1:
                for effectInstanceDice in level.criticalEffect:
                    if effectInstanceDice.effectUid == effect.effectId:
                        spellLevelsId = level.id
                        criticalEffect = True
        if spellLevelsId != -1:
            spellLevel = SpellLevel.getLevelById(spellLevelsId)
            effects = (
                spellLevel.effects if not criticalEffect else spellLevel.criticalEffect
            )
            for effid in effects:
                if effid.effectUid == effect.effectId:
                    buff.effect.triggers = effid.triggers
                    buff.effect.targetMask = effid.targetMask
                    buff.effect.effectElement = effid.effectElement
            buff.castingSpell.spellRank = spellLevel
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                "[BUFFS DEBUG]      Buff "
                + effect.uid
                + " : sort lanceur "
                + buff.castingSpell.spell.name
                + " ("
                + buff.castingSpell.spell.id
                + ") niveau "
                + buff.castingSpell.spellRank.grade
                + " par "
                + buff.castingSpell.casterId
            )
        return buff

    def decrementDuration(self, targetId: float) -> None:
        self.incrementDuration(targetId, -1)

    def synchronize(self) -> None:
        if GameDebugManager().buffsDebugActivated:
            logger.debug("[BUFFS DEBUG] Annulation du disabled sur tous les buffs")
        for entityId in self._buffs:
            for buffItem in self._buffs[entityId]:
                if buffItem.disabled:
                    buffItem.onReenable()

    def incrementDuration(
        self,
        targetId: float,
        delta: int,
        dispellEffect: bool = False,
        incrementMode: int = 1,
    ) -> None:
        modified: bool = False
        skipBuffUpdate: bool = False
        newBuffs: dict = dict()
        for targetBuffs in self._buffs:
            for buffItem in targetBuffs:
                if (
                    dispellEffect
                    and isinstance(buffItem, TriggeredBuff)
                    and buffItem.delay > 0
                ):
                    if newBuffs[buffItem.targetId] == None:
                        newBuffs[buffItem.targetId] = []
                    newBuffs[buffItem.targetId].append(buffItem)
                elif (
                    incrementMode == self.INCREMENT_MODE_SOURCE
                    and buffItem.aliveSource == targetId
                    or incrementMode == self.INCREMENT_MODE_TARGET
                    and buffItem.targetId == targetId
                ):
                    if incrementMode == self.INCREMENT_MODE_SOURCE and (
                        len(self.spellBuffsToIgnore) or buffItem.sourceJustReaffected
                    ):
                        skipBuffUpdate = False
                        for spell in self.spellBuffsToIgnore:
                            if (
                                spell.castingSpellId
                                == buffItem.castingSpell.castingSpellId
                                and spell.casterId == targetId
                            ):
                                skipBuffUpdate = True
                        if buffItem.sourceJustReaffected:
                            skipBuffUpdate = True
                            buffItem.sourceJustReaffected = False
                        if skipBuffUpdate:
                            if newBuffs[buffItem.targetId] == None:
                                newBuffs[buffItem.targetId] = []
                            newBuffs[buffItem.targetId].append(buffItem)
                            continue
                    modified = buffItem.incrementDuration(delta, dispellEffect)
                    if buffItem.active:
                        if newBuffs[buffItem.targetId] == None:
                            newBuffs[buffItem.targetId] = []
                        newBuffs[buffItem.targetId].append(buffItem)
                        if modified:
                            pass
                    else:
                        buffItem.onRemoved()
                else:
                    if newBuffs[buffItem.targetId] == None:
                        newBuffs[buffItem.targetId] = []
                    newBuffs[buffItem.targetId].append(buffItem)
        self._buffs = newBuffs
        fightEventsHelper.FightEventsHelper.sendAllFightEvent(True)

    def markFinishingBuffs(
        self, targetId: float, currentTurnIsEnding: bool = True
    ) -> None:
        fightBattleFrame: fightBattleFrame.FightBattleFrame = (
            Kernel().getWorker().getFrame(fightBattleFrame.FightBattleFrame)
        )
        fightersCount = len(fightBattleFrame.fighters)
        if fightBattleFrame is None:
            return
        currentFighterId: float = fightBattleFrame.currentPlayerId
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                f"[BUFFS DEBUG] Recherche des buffs de {targetId}"
                + " qui vont finir durant le tour  (combattant actuel "
                + str(currentFighterId)
                + ")    currentTurnIsEnding "
                + str(currentTurnIsEnding)
            )
        if self._buffs[targetId] == None:
            return
        for buffItem in self._buffs[targetId]:
            if buffItem.duration == 1:
                if GameDebugManager().buffsDebugActivated:
                    logger.debug(
                        "[BUFFS DEBUG]     - Buff "
                        + str(buffItem.uid)
                        + " n'a plus qu'un tour     (aliveSource "
                        + str(buffItem.aliveSource)
                        + "  sourceJustReaffected "
                        + str(buffItem.sourceJustReaffected)
                        + ")"
                    )
                buffWillEndBeforeTargetTurn = False
                casterIndex = -1
                targetIndex = -1
                currentFighterIndex = -1

                for i, fighterId in enumerate(fightBattleFrame.fightersList):
                    if fighterId == buffItem.aliveSource:
                        if buffItem.sourceJustReaffected:
                            buffItem.sourceJustReaffected = False
                        else:
                            casterIndex = i
                    if fighterId == buffItem.targetId:
                        targetIndex = i
                    if fighterId == currentFighterId:
                        currentFighterIndex = i
                if GameDebugManager().buffsDebugActivated:
                    logger.debug(
                        "[BUFFS DEBUG]             Index des combattants pour ce buff : lanceur "
                        + casterIndex
                        + ", cible "
                        + targetIndex
                        + "     combattant actuel "
                        + currentFighterIndex
                    )
                if casterIndex == -1 or targetIndex == -1 or currentFighterIndex == -1:
                    logger.warn(
                        "Error when marking finishing buff, fighters cannot be found "
                    )
                    return
                if casterIndex == targetIndex:
                    if currentFighterIndex == targetIndex and not currentTurnIsEnding:
                        if GameDebugManager().buffsDebugActivated:
                            logger.debug(
                                "[BUFFS DEBUG]                 cible = target = combattant actuel et ce n'est pas une fin de tour, on ne desactive pas"
                            )
                        continue
                    buffWillEndBeforeTargetTurn = True
                    if GameDebugManager().buffsDebugActivated:
                        logger.debug(
                            "[BUFFS DEBUG]                 cible = target, le buff doit etre desactiv�"
                        )
                elif currentFighterIndex == targetIndex and currentTurnIsEnding:
                    buffWillEndBeforeTargetTurn = True
                    if GameDebugManager().buffsDebugActivated:
                        logger.debug(
                            "[BUFFS DEBUG]                 fin du tour de la cible, le buff doit etre desactiv�"
                        )
                else:
                    if casterIndex > targetIndex:
                        if currentFighterIndex >= casterIndex:
                            currentFighterIndex -= fightersCount
                        casterIndex -= fightersCount
                    logger.debug(
                        "[BUFFS DEBUG]           --->  Index des combattants pour ce buff : lanceur "
                        + casterIndex
                        + ", cible "
                        + targetIndex
                        + "     combattant actuel "
                        + currentFighterIndex
                    )
                    if (
                        currentFighterIndex < casterIndex
                        or currentFighterIndex > targetIndex
                    ):
                        buffWillEndBeforeTargetTurn = True
                        if GameDebugManager().buffsDebugActivated:
                            logger.debug(
                                "[BUFFS DEBUG]                 le combattant actuel n'est pas entre le caster et la target, le buff doit etre desactiv�"
                            )
                if buffWillEndBeforeTargetTurn:
                    if GameDebugManager().buffsDebugActivated:
                        logger.debug(
                            "[BUFFS DEBUG]                   Buff "
                            + buffItem.uid
                            + " doit �tre d�sactiv�, il ne doit plus �tre affich� dans les stats du combattant"
                        )
                    basicBuff.BasicBuff(buffItem).onDisabled()

    def addBuff(self, buff: basicBuff.BasicBuff, applyBuff: bool = True) -> None:
        if not self._buffs[buff.targetId]:
            self._buffs[buff.targetId] = []
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                "[BUFFS DEBUG] Ajout du buff " + buff.uid + " sur " + buff.targetId
            )
        buffsCount: int = self._buffs[buff.targetId].length
        for i in range(buffsCount):
            actualBuff = self._buffs[buff.targetId][i]
            if buff.equals(actualBuff):
                sameBuff = actualBuff
            i += 1
        if not sameBuff or buff.actionId == ActionIds.ACTION_CHARACTER_BOOST_THRESHOLD:
            self._buffs[buff.targetId].append(buff)
        else:
            if (
                sameBuff is TriggeredBuff
                and sameBuff.effect.triggers.find("|") != -1
                or sameBuff.castingSpell.spellRank
                and sameBuff.castingSpell.spellRank.maxStack > 0
                and sameBuff.stack
                and len(sameBuff.stack) == sameBuff.castingSpell.spellRank.maxStack
            ):
                return
            sameBuff.add(buff)
        if applyBuff:
            buff.onApplied()
        if not sameBuff:
            pass
        else:
            pass

    def updateBuff(self, buff: basicBuff.BasicBuff) -> bool:
        targetId: float = buff.targetId
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                "[BUFFS DEBUG] Mise � jour du buff "
                + buff.uid
                + " sur "
                + buff.targetId
            )
        if not self._buffs[targetId]:
            return False
        i: int = self.getBuffIndex(targetId, buff.id)
        if i == -1:
            return False
        self._buffs[targetId][i].onRemoved()
        self._buffs[targetId][i].updateParam(
            buff.param1, buff.param2, buff.param3, buff.id
        )
        oldBuff = self._buffs[targetId][i]
        if not oldBuff:
            return False
        oldBuff.onApplied()
        pass
        return True

    def dispell(
        self,
        targetId: float,
        forceUndispellable: bool = False,
        critical: bool = False,
        dying: bool = False,
    ) -> None:
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                "[BUFFS DEBUG] Desenvoutement de tous les buffs de " + targetId
            )
        newBuffs: list = []
        for buff in self._buffs[targetId]:
            if buff.canBeDispell(forceUndispellable, int.MIN_VALUE, dying):
                if GameDebugManager().buffsDebugActivated:
                    logger.debug(
                        "[BUFFS DEBUG]      Buff " + buff.uid + " doit �tre retir�"
                    )
                pass
                buff.onRemoved()
            else:
                if GameDebugManager().buffsDebugActivated:
                    logger.debug("[BUFFS DEBUG]      Buff " + buff.uid + " reste")
                newBuffs.append(buff)
        self._buffs[targetId] = newBuffs

    def dispellSpell(
        self,
        targetId: float,
        spellId: int,
        forceUndispellable: bool = False,
        critical: bool = False,
        dying: bool = False,
    ) -> None:
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                "[BUFFS DEBUG] Desenvoutement de tous les buffs du sort "
                + spellId
                + " de "
                + targetId
            )
        newBuffs: list = []
        currentFighterId: float = CurrentPlayedFighterManager().currentFighterId
        for buff in self._buffs[targetId]:
            if spellId == buff.castingSpell.spell.id and buff.canBeDispell(
                forceUndispellable, int.MIN_VALUE, dying
            ):
                if GameDebugManager().buffsDebugActivated:
                    logger.debug(
                        "[BUFFS DEBUG]      Buff " + buff.uid + " doit �tre retir�"
                    )
                buff.onRemoved()
                pass
            else:
                if GameDebugManager().buffsDebugActivated:
                    logger.debug("[BUFFS DEBUG]      Buff " + buff.uid + " reste")
                newBuffs.append(buff)
        self._buffs[targetId] = newBuffs

    def dispellUniqueBuff(
        self,
        targetId: float,
        boostUID: int,
        forceUndispellable: bool = False,
        dying: bool = False,
        ultimateDebuff: bool = True,
    ) -> None:
        isState: bool = False
        i: int = self.getBuffIndex(targetId, boostUID)
        if i == -1:
            return
        buff: basicBuff.BasicBuff = self._buffs[targetId][i]
        if buff.canBeDispell(
            forceUndispellable, int(boostUID) if ultimateDebuff else -99999999, dying
        ):
            if buff.stack and len(buff.stack) > 1 and not dying:
                if GameDebugManager().buffsDebugActivated:
                    logger.debug(
                        "[BUFFS DEBUG] Desenvoutement du buff stack� "
                        + boostUID
                        + " de "
                        + targetId
                    )
                buff.onRemoved()
                isState = False
                if buff.actionId == ActionIds.ACTION_BOOST_SPELL_BASE_DMG:
                    buff.param1 = buff.stack[0].param1
                    buff.param2 -= buff.stack[0].param2
                    buff.param3 -= buff.stack[0].param3
                if buff.actionId == ActionIds.ACTION_CHARACTER_PUNISHMENT:
                    buff.param1 -= buff.stack[0].param2
                if (
                    buff.actionId == ActionIds.ACTION_FIGHT_SET_STATE
                    or buff.actionId == ActionIds.ACTION_FIGHT_UNSET_STATE
                ):
                    isState = True
                else:
                    buff.param1 -= buff.stack[0].param1
                    buff.param2 -= buff.stack[0].param2
                    buff.param3 -= buff.stack[0].param3
                buff.stack.pop(0)
                buff.refreshDescription()
                if not isState:
                    buff.onApplied()
                pass
            else:
                pass
                if GameDebugManager().buffsDebugActivated:
                    logger.debug(
                        "[BUFFS DEBUG] Desenvoutement du buff "
                        + str(boostUID)
                        + " de "
                        + str(targetId)
                    )
                self._buffs[targetId].splice(self._buffs[targetId].find(buff), 1)
                buff.onRemoved()
                if targetId == CurrentPlayedFighterManager().currentFighterId:
                    SpellWrapper.refreshAllPlayerSpellHolder(targetId)

    def removeLinkedBuff(
        self, sourceId: float, forceUndispellable: bool = False, dying: bool = False
    ) -> list:
        impactedTarget: list = []
        entitiesFrame = (
            Kernel().getWorker().getFrame(fightEntitiesFrame.FightEntitiesFrame)
        )
        fightBattleFrame: fightBattleFrame.FightBattleFrame = (
            Kernel().getWorker().getFrame(fightBattleFrame.FightBattleFrame)
        )
        infos: GameFightFighterInformations = entitiesFrame.getEntityInfos(sourceId)
        if GameDebugManager().buffsDebugActivated:
            logger.debug("[BUFFS DEBUG] Retrait des buffs lanc�s par " + sourceId)
        for buffList in self._buffs:
            buffListCopy = []
            for buff in buffList:
                buffListCopy.append(buff)
            for buff in buffListCopy:
                if buff.source == sourceId:
                    if GameDebugManager().buffsDebugActivated:
                        logger.debug(
                            "[BUFFS DEBUG]      Buff "
                            + str(buff.uid)
                            + " doit �tre retir�"
                        )
                    self.dispellUniqueBuff(
                        buff.targetId, buff.id, forceUndispellable, dying, False
                    )
                    if impactedTarget.find(buff.targetId) == -1:
                        impactedTarget.append(buff.targetId)
                    if (
                        dying
                        and infos.stats.summoned
                        and infos.stats.summoner != fightBattleFrame.currentPlayerId
                    ):
                        buff.aliveSource = infos.stats.summoner
                        if GameDebugManager().buffsDebugActivated:
                            logger.debug(
                                "[BUFFS DEBUG]      Buff "
                                + buff.uid
                                + " doit �tre reaffect� � l'invocateur "
                                + infos.stats.summoner
                            )
        return impactedTarget

    def reaffectBuffs(self, sourceId: float) -> None:
        entity: GameFightFighterInformations = self.fightEntitiesFrame.getEntityInfos(
            sourceId
        )
        if entity.stats.summoned:
            next = self.getNextFighter(sourceId)
            if GameDebugManager().buffsDebugActivated:
                logger.debug(
                    "[BUFFS DEBUG] R�affectation des buffs lanc�s par "
                    + sourceId
                    + ", le nouveau 'lanceur' sera "
                    + next
                )
            frame = Kernel().getWorker().getFrame(fightBattleFrame.FightBattleFrame)
            dontDecrementBuffThisTurn = False
            if frame.currentPlayerId == sourceId:
                dontDecrementBuffThisTurn = True
            for buffList in self._buffs:
                for buff in buffList:
                    if buff.aliveSource == sourceId:
                        if GameDebugManager().buffsDebugActivated:
                            logger.debug(
                                "[BUFFS DEBUG]      Buff "
                                + buff.uid
                                + " doit �tre reaffect�"
                            )
                        buff.aliveSource = next
                        buff.sourceJustReaffected = dontDecrementBuffThisTurn

    def getNextFighter(self, sourceId: float) -> float:
        frame: fightBattleFrame.FightBattleFrame = (
            Kernel().getWorker().getFrame(fightBattleFrame.FightBattleFrame)
        )
        if frame is None:
            return 0
        found: bool = False
        for fighter in frame.fightersList:
            if found:
                return fighter
            if fighter == sourceId:
                found = True
        if found:
            return frame.fightersList[0]
        return 0

    def getFighterInfo(self, targetId: float) -> GameFightFighterInformations:
        return self.fightEntitiesFrame.getEntityInfos(targetId)

    def getAllBuff(self, targetId: float) -> list:
        return self._buffs[targetId]

    def getLifeThreshold(self, targetId: float) -> int:
        targetBuffs: list = self._buffs[targetId]
        if not targetBuffs:
            return 0
        for index in range(len(targetBuffs)):
            buff = targetBuffs[index]
            if (
                buff
                and not buff.removed
                and buff.actionId == ActionIdProtocol.ACTION_CHARACTER_BOOST_THRESHOLD
                and isinstance(buff, StatBuff)
            ):
                lifeThreshold = max(lifeThreshold, buff)
        return lifeThreshold

    def resetTriggerCount(self, targetId: float) -> bool:
        for buff in self._buffs[targetId]:

            if isinstance(buff, TriggeredBuff):
                TriggeredBuff(buff).triggerCount = 0
                return True
        return False

    def getBuff(self, buffId: int, playerId: float) -> basicBuff.BasicBuff:
        for buff in self._buffs[playerId]:
            if buffId == buff.id:
                return buff
        return None

    @property
    def fightEntitiesFrame(self) -> fightEntitiesFrame.FightEntitiesFrame:
        return Kernel().getWorker().getFrame(fightEntitiesFrame.FightEntitiesFrame)

    def getBuffIndex(self, targetId: float, buffId: int) -> int:
        for i in self._buffs[targetId]:
            if buffId == self._buffs[targetId][i].id:
                return int(i)
            for subBuff in self._buffs[targetId][i].stack:
                if buffId == subBuff.id:
                    return int(i)
        return -1

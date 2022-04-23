from typing import Any
from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDice import (
    EffectInstanceDice,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceInteger import (
    EffectInstanceInteger,
)
from com.ankamagames.dofus.datacenter.spells.SpellLevel import SpellLevel
from com.ankamagames.dofus.enums.ActionIds import ActionIds
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
import com.ankamagames.dofus.logic.game.fight.frames.FightBattleFrame as fightBattleFrame
import com.ankamagames.dofus.logic.game.fight.frames.FightEntitiesFrame as fightBattleFrame
from com.ankamagames.dofus.logic.game.fight.types.CastingSpell import CastingSpell
from com.ankamagames.dofus.misc.utils.GameDebugManager import GameDebugManager
from com.ankamagames.dofus.network.enums.FightDispellableEnum import (
    FightDispellableEnum,
)
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import (
    AbstractFightDispellableEffect,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import (
    GameFightFighterInformations,
)
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class BasicBuff:

    _effect: EffectInstance

    _disabled: bool = False

    _removed: bool = False

    uid: int

    duration: int

    castingSpell: CastingSpell

    targetId: float

    critical: bool = False

    dispelable: int

    actionId: int

    id: int

    source: float

    aliveSource: float

    sourceJustReaffected: bool = False

    stack: list["BasicBuff"]

    parentBoostUid: int

    dataUid: int

    def __init__(
        self,
        effect: AbstractFightDispellableEffect = None,
        castingSpell: CastingSpell = None,
        actionId: int = 0,
        param1=None,
        param2=None,
        param3=None,
    ):
        super().__init__()
        if not effect:
            return
        self.id = effect.uid
        self.uid = effect.uid
        self.actionId = actionId
        self.targetId = effect.targetId
        self.castingSpell = castingSpell
        self.duration = effect.turnDuration
        self.dispelable = effect.dispelable
        self.source = castingSpell.casterId
        self.dataUid = effect.effectId
        fightBattleFrame = (
            Kernel().getWorker().getFrame(fightBattleFrame.FightBattleFrame)
        )
        currentPlayerId: float = fightBattleFrame.currentPlayerId
        isPlayerId = currentPlayerId is not 0
        fighterInfo: GameFightFighterInformations = None
        if isPlayerId:
            entitiesFrame = Kernel().getWorker().getFrame(fightBattleFrame.FightEntitiesFrame)
            if entitiesFrame is not None:
                fighterInfo = entitiesFrame.getEntityInfos(currentPlayerId)
        if (
            Kernel().beingInReconection
            or not isPlayerId
            or fighterInfo is not None
            and not fighterInfo.spawnInfo.alive
        ):
            self.aliveSource = self.source
        else:
            self.aliveSource = currentPlayerId
        self.parentBoostUid = self.parentBoostUid
        self.initParam(param1, param2, param3)
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                f"[BUFFS DEBUG] Buff {self.id} créé ! Params {param1}, {param2}, {param3}, aliveSource {self.aliveSource} '{self._effect.description}'"
            )

    @property
    def effect(self) -> EffectInstance:
        return self._effect

    @property
    def type(self) -> str:
        return "BasicBuff"

    @property
    def param1(self) -> Any:
        if isinstance(self._effect, EffectInstanceDice):
            return EffectInstanceDice(self._effect).diceNum
        return None

    @property
    def param2(self) -> Any:
        if isinstance(self._effect, EffectInstanceDice):
            return EffectInstanceDice(self._effect).diceSide
        return None

    @property
    def param3(self) -> Any:
        if isinstance(self._effect, EffectInstanceInteger):
            return EffectInstanceInteger(self._effect).value
        return None

    @param1.setter
    def param1(self, v) -> None:
        self._effect.setParameter(0, None if v == 0 else v)

    @param2.setter
    def param2(self, v) -> None:
        self._effect.setParameter(1, None if v == 0 else v)

    @param3.setter
    def param3(self, v) -> None:
        self._effect.setParameter(2, None if v == 0 else v)

    @property
    def rawParam1(self) -> Any:
        return self._rawParam1

    @property
    def rawParam2(self) -> Any:
        return self._rawParam2

    @property
    def rawParam3(self) -> Any:
        return self._rawParam3

    @property
    def unusableNextTurn(self) -> bool:
        if self.duration > 1 or self.duration < 0:
            return False
        frame = Kernel().getWorker().getFrame(fightBattleFrame.FightBattleFrame)
        if frame:
            currentPlayerId = frame.currentPlayerId
            playerId = PlayedCharacterManager().id
            if currentPlayerId == playerId or currentPlayerId == self.source:
                return False
            playerPos = -1
            currentPos = -1
            casterPos = -1
            for i in range(len(frame.fightersList)):
                fighter = frame.fightersList[i]
                if fighter == playerId:
                    playerPos = i
                if fighter == currentPlayerId:
                    currentPos = i
                if fighter == self.source:
                    casterPos = i
            if casterPos < currentPos:
                casterPos += len(frame.fightersList)
            if playerPos < currentPos:
                playerPos += len(frame.fightersList)
            return not (playerPos > currentPos and playerPos <= casterPos)
        return False

    @property
    def trigger(self) -> bool:
        return False

    @property
    def effectOrder(self) -> int:
        effect: EffectInstance = None
        for i in range(len(self.castingSpell.spellRank.effects)):
            effect = self.castingSpell.spellRank.effects[i]
            if effect.effectUid == self.dataUid:
                return i
        return -1

    @property
    def disabled(self) -> bool:
        return self._disabled

    def initParam(self, param1: int, param2: int, param3: int) -> None:
        sl: SpellLevel = None
        slId: int = 0
        foundEi: EffectInstanceDice = None
        forceBuffsShowInUI: bool = GameDebugManager().detailedFightLog_showBuffsInUi
        forceBuffsShowInFightLog: bool = (
            GameDebugManager().detailedFightLog_showEverything
        )
        if param1 and param1 != 0 or param2 and param2 != 0:
            self._rawParam1 = param1
            self._rawParam2 = param2
            self._rawParam3 = param3
            self._effect = EffectInstanceDice()
            self._effect.effectUid = self.dataUid
            self._effect.effectId = self.actionId
            self._effect.duration = self.duration
            self._effect.diceNum = param1
            self._effect.diceSide = param2
            self._effect.value = param3
            self._effect.trigger = self.trigger
        else:
            self._rawParam3 = param3
            self._effect = EffectInstanceInteger()
            self._effect.dispellable = self.dispelable
            self._effect.effectUid = self.dataUid
            self._effect.effectId = self.actionId
            self._effect.duration = self.duration
            self._effect.value = param3
            self._effect.trigger = self.trigger
        for slId in self.castingSpell.spell.spellLevels:
            sl = SpellLevel.getLevelById(slId)
            if sl:
                foundEi = self.findEffectOnSpellList(self.dataUid, sl.effects)
                if foundEi == None:
                    foundEi = self.findEffectOnSpellList(
                        self.dataUid, sl.criticalEffect
                    )
                if foundEi:
                    self._effect.visibleInTooltip = foundEi.visibleInTooltip
                    self._effect.visibleInBuffUi = (
                        True if forceBuffsShowInUI else bool(foundEi.visibleInBuffUi)
                    )
                    self._effect.visibleInFightLog = (
                        True
                        if forceBuffsShowInFightLog
                        else bool(foundEi.visibleInFightLog)
                    )
                    self._effect.order = foundEi.order

    def findEffectOnSpellList(
        self, id: int, list: list[EffectInstanceDice]
    ) -> EffectInstanceDice:
        for i in range(len(list)):
            if list[i].effectUid == id:
                return list[i]
        return None

    def canBeDispell(
        self,
        forceUndispellable: bool = False,
        targetBuffId: int = -2147483648,
        dying: bool = False,
    ) -> bool:
        if targetBuffId == self.id:
            return True
        if self.dispelable == FightDispellableEnum.DISPELLABLE:
            return True
        if self.dispelable == FightDispellableEnum.DISPELLABLE_BY_STRONG_DISPEL:
            return forceUndispellable
        if self.dispelable == FightDispellableEnum.DISPELLABLE_BY_DEATH:
            return dying or forceUndispellable
        if self.dispelable == FightDispellableEnum.REALLY_NOT_DISPELLABLE:
            return targetBuffId == self.id
        else:
            return False

    def dispellableByDeath(self) -> bool:
        return (
            self.dispelable == FightDispellableEnum.DISPELLABLE_BY_DEATH
            or self.dispelable == FightDispellableEnum.DISPELLABLE
        )

    def onDisabled(self) -> None:
        if GameDebugManager().buffsDebugActivated:
            logger.debug("[BUFFS DEBUG] Buff {self.uid} desactiv�")
        self._disabled = True

    @property
    def removed(self) -> bool:
        return self._removed

    def onReenable(self) -> None:
        if not self._removed:
            if GameDebugManager().buffsDebugActivated:
                logger.debug("[BUFFS DEBUG] Buff {self.uid} r�activ�")
            self._disabled = False

    def onRemoved(self) -> None:
        if GameDebugManager().buffsDebugActivated:
            logger.debug("[BUFFS DEBUG] Buff {self.uid} retir�")
        self._removed = True
        if not self._disabled:
            self.onDisabled()

    def onApplied(self) -> None:
        if GameDebugManager().buffsDebugActivated:
            logger.debug("[BUFFS DEBUG] Buff {self.uid} appliqu�")
        self._disabled = False
        self._removed = False

    def equals(self, other: "BasicBuff", ignoreSpell: bool = False) -> bool:
        sb1: StateBuff = None
        sb2: StateBuff = None
        if (
            self.targetId != other.targetId
            or self.aliveSource != other.aliveSource
            or self.effect.effectId != other.actionId
            or self.duration != other.duration
            or self.effect.hasOwnProperty("delay")
            and other.effect.hasOwnProperty("delay")
            and self.effect.delay != other.effect.delay
            or self.castingSpell.spellRank
            and other.castingSpell.spellRank
            and not ignoreSpell
            and self.castingSpell.spellRank.id != other.castingSpell.spellRank.id
            or not ignoreSpell
            and self.castingSpell.spell.id != other.castingSpell.spell.id
            or getQualifiedClassName(self) != getQualifiedClassName(other)
            or self.source != other.source
            or self.trigger
            and (self.effect.triggers.find("|") == -1 or self.dataUid != other.dataUid)
        ):
            return False
        if self.actionId == ActionIds.ACTION_CHARACTER_PUNISHMENT:
            if self.param1 != other.param1:
                return False
        elif (
            self.actionId == ActionIds.ACTION_BOOST_SPELL_RANGE_MAX
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_RANGE_MIN
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_RANGEABLE
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_DMG
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_HEAL
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_AP_COST
            or self.actionId == ActionIds.ACTION_DEBOOST_SPELL_AP_COST
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_CAST_INTVL
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_CC
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_CASTOUTLINE
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_NOLINEOFSIGHT
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_MAXPERTURN
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_MAXPERTARGET
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_CAST_INTVL_SET
            or self.actionId == ActionIds.ACTION_BOOST_SPELL_BASE_DMG
            or self.actionId == ActionIds.ACTION_DEBOOST_SPELL_RANGE_MAX
            or self.actionId == ActionIds.ACTION_DEBOOST_SPELL_RANGE_MIN
            or self.actionId == ActionIds.ACTION_CHARACTER_DISPELL_SPELL
            or self.actionId == ActionIds.ACTION_TARGET_EXECUTE_SPELL
            or self.actionId == ActionIds.ACTION_TARGET_EXECUTE_SPELL_WITH_ANIMATION
            or self.actionId == ActionIds.ACTION_TARGET_EXECUTE_SPELL_ON_SOURCE
            or self.actionId == ActionIds.ACTION_SOURCE_EXECUTE_SPELL_ON_TARGET
            or self.actionId == ActionIds.ACTION_SOURCE_EXECUTE_SPELL_ON_SOURCE
            or self.actionId == ActionIds.ACTION_CHARACTER_ADD_SPELL_COOLDOWN
            or self.actionId == ActionIds.ACTION_CHARACTER_REMOVE_SPELL_COOLDOWN
            or self.actionId == ActionIds.ACTION_CHARACTER_PROTECTION_FROM_SPELL
            or self.actionId == ActionIds.ACTION_CHARACTER_SET_SPELL_COOLDOWN
        ):
            if self.param1 != other.param1:
                return False
        else:
            if (
                self.actionId
                == ActionIds.ACTION_CHARACTER_BOOST_ONE_WEAPON_DAMAGE_PERCENT
            ):
                return False
            if self.actionId == ActionIds.ACTION_CHARACTER_ADD_APPEARANCE:
                if self.dataUid != other.dataUid:
                    return False
            elif self.actionId == other.actionId and (
                self.actionId == ActionIds.ACTION_FIGHT_DISABLE_STATE
                or self.actionId == ActionIds.ACTION_FIGHT_UNSET_STATE
                or self.actionId == ActionIds.ACTION_FIGHT_SET_STATE
            ):
                sb1 = self
                sb2 = other
                if sb1 and sb2:
                    if sb1.stateId != sb2.stateId:
                        return False
        return True

    def add(self, buff: "BasicBuff") -> None:
        if not self.stack:
            self.stack = list[BasicBuff]()
            self.stack.append(self.clone(self.id))
        self.stack.append(buff)
        additionDetails: str = ""
        if self.actionId in [
            ActionIds.ACTION_BOOST_SPELL_BASE_DMG,
            ActionIds.ACTION_BOOST_SPELL_RANGE_MAX,
            ActionIds.ACTION_BOOST_SPELL_RANGE_MIN,
            ActionIds.ACTION_BOOST_SPELL_RANGEABLE,
            ActionIds.ACTION_BOOST_SPELL_DMG,
            ActionIds.ACTION_BOOST_SPELL_HEAL,
            ActionIds.ACTION_BOOST_SPELL_AP_COST,
            ActionIds.ACTION_DEBOOST_SPELL_AP_COST,
            ActionIds.ACTION_BOOST_SPELL_CAST_INTVL,
            ActionIds.ACTION_BOOST_SPELL_CC,
            ActionIds.ACTION_BOOST_SPELL_CASTOUTLINE,
            ActionIds.ACTION_BOOST_SPELL_NOLINEOFSIGHT,
            ActionIds.ACTION_BOOST_SPELL_MAXPERTURN,
            ActionIds.ACTION_BOOST_SPELL_MAXPERTARGET,
            ActionIds.ACTION_BOOST_SPELL_CAST_INTVL_SET,
            ActionIds.ACTION_DEBOOST_SPELL_RANGE_MAX,
            ActionIds.ACTION_DEBOOST_SPELL_RANGE_MIN,
        ]:
            additionDetails += (
                f"\rparam2 : {self.param2}  & {(self.param2 + buff.param2)}"
            )
            additionDetails += (
                f"\rparam3 : {self.param3}  & {(self.param3 + buff.param3)}"
            )
            self.param1 = buff.param1
            self.param2 += buff.param2
            self.param3 += buff.param3
        if self.actionId == ActionIds.ACTION_CHARACTER_PUNISHMENT:
            additionDetails += (
                f"\rparam1 : {self.param1}  &  {(self.param1 + buff.param2)}"
            )
            self.param1 += buff.param2

        if self.actionId in [
            ActionIds.ACTION_FIGHT_SET_STATE,
            ActionIds.ACTION_FIGHT_UNSET_STATE,
            ActionIds.ACTION_FIGHT_DISABLE_STATE,
        ]:
            if isinstance(self, StateBuff) and isinstance(buff, StateBuff):
                additionDetails += f"\rdelta : {self.delta} à {self.delta + buff}"
                self.delta += buff.delta

        else:
            additionDetails += f"\rparam1 : {self.param1} à {self.param1 + buff.param1}"
            additionDetails += f"\rparam2 : {self.param2} à {self.param2 + buff.param2}"
            additionDetails += f"\rparam3 : {self.param3} à {self.param3 + buff.param3}"
            self.param1 += buff.param1
            self.param2 += buff.param2
            self.param3 += buff.param3
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                "[BUFFS DEBUG] Buff {self.uid} : ajout du buff {buff.uid} {additionDetails}"
            )
        self.refreshDescription()

    def updateParam(
        self, value1: int = 0, value2: int = 0, value3: int = 0, buffId: int = -1
    ) -> None:
        if buffId == -1:
            p1 = value1
            p2 = value2
            p3 = value3
        elif self.stack and len(self.stack) > 1:
            if self.id == buffId:
                for stackBuff in self.stack.reverse():
                    if value1 > stackBuff.param1:
                        value1 -= stackBuff.param1
                        stackBuff.param1 = 0
                    elif value1 > 0:
                        stackBuff.param1 = value1
                        value1 = 0
                    if value2 > stackBuff.param2:
                        value2 -= stackBuff.param2
                        stackBuff.param2 = 0
                    elif value2 > 0:
                        stackBuff.param2 = value2
                        value2 = 0
                    if value3 > stackBuff.param3:
                        value3 -= stackBuff.param3
                        stackBuff.param3 = 0
                    elif value3 > 0:
                        stackBuff.param3 = value3
                        value3 = 0
                    p1 += stackBuff.param1
                    p2 += stackBuff.param2
                    p3 += stackBuff.param3
            else:
                for stackBuff in self.stack:
                    if stackBuff.id != buffId:
                        continue
                    if stackBuff.actionId in [
                        ActionIds.ACTION_CHARACTER_PUNISHMENT,
                        ActionIds.ACTION_FIGHT_SET_STATE,
                        ActionIds.ACTION_FIGHT_UNSET_STATE,
                        ActionIds.ACTION_FIGHT_DISABLE_STATE,
                    ]:
                        break
                    else:
                        stackBuff.param1 = value1
                        stackBuff.param2 = value2
                        stackBuff.param3 = value3
                    p1 += stackBuff.param1
                    p2 += stackBuff.param2
                    p3 += stackBuff.param3
        else:
            p1 = value1
            p2 = value2
            p3 = value3
        if self.actionId == ActionIds.ACTION_CHARACTER_PUNISHMENT:
            self.param1 = p2
        if self.actionId in [
            ActionIds.ACTION_FIGHT_SET_STATE,
            ActionIds.ACTION_FIGHT_UNSET_STATE,
            ActionIds.ACTION_FIGHT_DISABLE_STATE,
        ]:
            pass
        else:
            self.param1 = p1
            self.param2 = p2
            self.param3 = p3
        if GameDebugManager().buffsDebugActivated:
            logger.debug(
                "[BUFFS DEBUG] Buff "
                + self.id
                + " rafraichissement des params "
                + self.param1
                + ", "
                + self.param2
                + ", "
                + self.param3
            )
        self.refreshDescription()

    def refreshDescription(self) -> None:
        self._effect.forceDescriptionRefresh()

    def incrementDuration(self, delta: int, dispellEffect: bool = False) -> bool:
        oldDuration: int = 0
        if GameDebugManager().buffsDebugActivated:
            if dispellEffect:
                logger.debug(
                    f"[BUFFS DEBUG] Buff {self.id} durée modifiée de {delta} (desenvoutement de l'effet)"
                )
        if not dispellEffect or self.canBeDispell():
            if self.duration >= 63 or self.duration == -1000:
                return False
            oldDuration = self.duration
            if self.duration + delta > 0:
                self.duration += delta
                self.effect.duration += delta
                if GameDebugManager().buffsDebugActivated:
                    logger.debug(
                        f"[BUFFS DEBUG] Buff {self.id} durée modifiée de {oldDuration} à {self.duration}"
                    )
                return True
            if self.duration > 0:
                self.duration = 0
                self.effect.duration = 0
                if GameDebugManager().buffsDebugActivated:
                    logger.debug(
                        f"[BUFFS DEBUG] Buff {self.id} durée modifiée de {oldDuration} à {self.duration}"
                    )
                return True
            return False
        return False

    @property
    def active(self) -> bool:
        return self.duration != 0

    def clone(self, id: int = 0) -> "BasicBuff":
        bb: BasicBuff = BasicBuff()
        bb.id = self.uid
        bb.uid = self.uid
        bb.dataUid = self.dataUid
        bb.actionId = self.actionId
        bb.targetId = self.targetId
        bb.castingSpell = self.castingSpell
        bb.duration = self.duration
        bb.dispelable = self.dispelable
        bb.source = self.source
        bb.aliveSource = self.aliveSource
        bb.sourceJustReaffected = self.sourceJustReaffected
        bb.parentBoostUid = self.parentBoostUid
        bb.initParam(self.param1, self.param2, self.param3)
        return bb

    def __str__(self) -> str:
        return f"[BasicBuff id={self.id}, uid={self.uid}, targetId={self.targetId}, sourceId={self.source}, duration={self.duration}, len(stack)={(len(self.stack) if self.stack else 0)}]"

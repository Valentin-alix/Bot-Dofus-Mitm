from threading import Timer
from time import perf_counter
from types import FunctionType
from com.ankamagames.atouin.managers.EntitiesManager import EntitiesManager
from com.ankamagames.atouin.utils.DataMapProvider import DataMapProvider
import com.ankamagames.dofus.internalDatacenter.spells.SpellWrapper as spellwrapper
from com.ankamagames.dofus.internalDatacenter.stats.EntityStats import EntityStats
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
import com.ankamagames.dofus.logic.game.common.frames.PlayedCharacterUpdatesFrame as pcuF
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
import com.ankamagames.dofus.logic.game.fight.fightEvents.FightEventsHelper as fightEventsHelper
import com.ankamagames.dofus.logic.game.fight.frames.FightContextFrame as fightContextFrame
import com.ankamagames.dofus.logic.game.fight.frames.FightEntitiesFrame as fightEntitiesFrame
from com.ankamagames.dofus.logic.game.fight.frames.FightSequenceFrame import (
    FightSequenceFrame,
)
from com.ankamagames.dofus.logic.game.fight.managers.BuffManager import BuffManager
from com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import (
    CurrentPlayedFighterManager,
)
from com.ankamagames.dofus.logic.game.fight.managers.FightersStateManager import (
    FightersStateManager,
)
from com.ankamagames.dofus.logic.game.fight.managers.SpellCastInFightManager import (
    SpellCastInFightManager,
)
from com.ankamagames.dofus.logic.game.fight.types.BasicBuff import BasicBuff
from com.ankamagames.dofus.logic.game.fight.types.StatBuff import StatBuff
from com.ankamagames.dofus.misc.utils.GameDebugManager import GameDebugManager
from com.ankamagames.dofus.network.messages.game.actions.GameActionAcknowledgementMessage import (
    GameActionAcknowledgementMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionUpdateEffectTriggerCountMessage import (
    GameActionUpdateEffectTriggerCountMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.sequence.SequenceEndMessage import (
    SequenceEndMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.sequence.SequenceStartMessage import (
    SequenceStartMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterStatsListMessage import (
    CharacterStatsListMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.UpdateSpellModifierMessage import (
    UpdateSpellModifierMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextDestroyMessage import (
    GameContextDestroyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import (
    GameFightEndMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightLeaveMessage import (
    GameFightLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightNewRoundMessage import (
    GameFightNewRoundMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightNewWaveMessage import (
    GameFightNewWaveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPauseMessage import (
    GameFightPauseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSynchronizeMessage import (
    GameFightSynchronizeMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnEndMessage import (
    GameFightTurnEndMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnListMessage import (
    GameFightTurnListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnReadyMessage import (
    GameFightTurnReadyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnReadyRequestMessage import (
    GameFightTurnReadyRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnResumeMessage import (
    GameFightTurnResumeMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartMessage import (
    GameFightTurnStartMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartPlayingMessage import (
    GameFightTurnStartPlayingMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.SlaveNoLongerControledMessage import (
    SlaveNoLongerControledMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.SlaveSwitchContextMessage import (
    SlaveSwitchContextMessage,
)
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import (
    GameContextActorInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacterInformations import (
    GameFightCharacterInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import (
    GameFightEffectTriggerCount,
)
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import (
    GameFightFighterInformations,
)
from com.ankamagames.dofus.types.entities.AnimatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.benchmark.BenchmarkTimer import BenchmarkTimer
from com.ankamagames.jerakine.handlers.messages.Action import Action
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.sequencer.SerialSequencer import SerialSequencer
from com.ankamagames.jerakine.types.enums.Priority import Priority

logger = Logger(__name__)


class FightBattleFrame(Frame):

    FIGHT_SEQUENCER_NAME: str = "FightBattleSequencer"

    isFightAboutToEnd: bool = False

    _sequenceFrameSwitcher: FightSequenceSwitcherFrame

    _turnFrame: FightTurnFrame

    _currentSequenceFrame: FightSequenceFrame

    _sequenceFrames: list

    _executingSequence: bool

    _confirmTurnEnd: bool

    _endBattle: bool

    _battleResults: GameFightEndMessage

    _refreshTurnsList: bool

    _newTurnsList: list[float]

    _newDeadTurnsList: list[float]

    _turnsList: list[float]

    _deadTurnsList: list[float]

    _playerTargetedEntitiesList: list[float]

    _fightIsPaused: bool = False

    _deathPlayingNumber: int = 0

    _synchroniseFighters: list[GameFightFighterInformations] = None

    _synchroniseFightersInstanceId: int = 4.294967295e9

    _neverSynchronizedBefore: bool = True

    _delayCslmsg: CharacterStatsListMessage

    _playerNewTurn: AnimatedCharacter

    _turnsCount: int = 0

    _destroyed: bool

    _playingSlaveEntity: bool = False

    _lastPlayerId: float

    _nextLastPlayerId: float

    _currentPlayerId: float = 0

    _skipTurnTimer: BenchmarkTimer

    _masterId: float

    _slaveId: float

    _autoEndTurn: bool = False

    _autoEndTurnTimer: BenchmarkTimer

    _newWave: bool

    _newWaveId: int

    _sequenceFrameCached: FightSequenceFrame = None

    def __init__(self):
        self._playerTargetedEntitiesList = list[float](0)
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.HIGH

    @property
    def fightIsPaused(self) -> bool:
        return self._fightIsPaused

    @property
    def fightersList(self) -> list[float]:
        return self._turnsList

    @fightersList.setter
    def fightersList(self, turnList: list[float]) -> None:
        self._turnsList = turnList

    @property
    def deadFightersList(self) -> list[float]:
        return self._deadTurnsList

    @deadFightersList.setter
    def deadFightersList(self, deadTurnList: list[float]) -> None:
        self._deadTurnsList = deadTurnList

    @property
    def targetedEntities(self) -> list[float]:
        return self._playerTargetedEntitiesList

    @property
    def turnsCount(self) -> int:
        return self._turnsCount

    @turnsCount.setter
    def turnsCount(self, turn: int) -> None:
        self._turnsCount = turn

    @property
    def currentPlayerId(self) -> float:
        return self._currentPlayerId

    @property
    def executingSequence(self) -> bool:
        return self._executingSequence

    @property
    def currentSequenceFrame(self) -> FightSequenceFrame:
        return self._currentSequenceFrame

    @property
    def playingSlaveEntity(self) -> bool:
        return self._playingSlaveEntity

    @property
    def slaveId(self) -> float:
        return self._slaveId

    @property
    def masterId(self) -> float:
        return self._masterId

    @property
    def deathPlayingNumber(self) -> int:
        return self._deathPlayingNumber

    @deathPlayingNumber.setter
    def deathPlayingNumber(self, n: int) -> None:
        self._deathPlayingNumber = n

    def pushed(self) -> bool:
        self._turnFrame = FightTurnFrame()
        self._playingSlaveEntity = False
        self._sequenceFrames = []
        DataMapProvider().isInFight = True
        krnl.Kernel().getWorker().addFrame(self._turnFrame)
        self._destroyed = False
        self._autoEndTurnTimer = Timer(0.06, self.sendAutoEndTurn)
        self._neverSynchronizedBefore = True
        return True

    def process(self, msg: Message) -> bool:

        if isinstance(msg, GameFightTurnListMessage):
            gftmsg = msg
            if self._executingSequence or self._currentSequenceFrame:
                logger.warn(
                    "There was a turns list update during self sequence... Let's wait its finish before doing it."
                )
                self._refreshTurnsList = True
                self._newTurnsList = gftmsg.ids
                self._newDeadTurnsList = gftmsg.deadsIds
            else:
                self.updateTurnsList(gftmsg.ids, gftmsg.deadsIds)
            return True

        if isinstance(msg, GameFightSynchronizeMessage):
            gftcimsg = msg
            if self._newWave:
                for fighter in gftcimsg.fighters:
                    if (
                        fighter.spawnInfo.alive
                        and fighter.wave == self._newWaveId
                        and not fightEntitiesFrame.FightEntitiesFrame.getCurrentInstance().getEntityInfos(
                            fighter.contextualId
                        )
                    ):
                        fightEntitiesFrame.FightEntitiesFrame.getCurrentInstance().registerActor(
                            fighter
                        )
            if self._executingSequence:
                self._synchroniseFighters = gftcimsg.fighters
                self._synchroniseFightersInstanceId = (
                    FightSequenceFrame.currentInstanceId
                )
            else:
                self.gameFightSynchronize(gftcimsg.fighters)
            return False

        if isinstance(msg, GameActionUpdateEffectTriggerCountMessage):
            gauetcmsg = msg
            for effectTrigger in gauetcmsg.targetIds:
                for buffTriggered in BuffManager().getAllBuff(effectTrigger.targetId):
                    if (
                        buffTriggered is TriggeredBuff
                        and buffTriggered.effect.effectUid == effectTrigger.effectId
                    ):
                        buffTriggered.triggerCount = effectTrigger.count
            return True

        if isinstance(msg, SlaveSwitchContextMessage):
            sscmsg = msg
            playerId = PlayedCharacterManager().id
            if sscmsg.masterId == playerId:
                self._masterId = sscmsg.masterId
                self._slaveId = sscmsg.slaveId
                if not self._currentPlayerId and self._turnsList.find(
                    self._masterId
                ) > self._turnsList.find(self._slaveId):
                    self.prepareNextPlayableCharacter(self._masterId)
            return False

        if isinstance(msg, SlaveNoLongerControledMessage):
            snlcmsg = msg
            playerId = PlayedCharacterManager().id
            if snlcmsg.masterId != playerId and self._slaveId == snlcmsg.slaveId:
                self._masterId = playerId
                self._slaveId = self._masterId
                self.prepareNextPlayableCharacter(playerId)
                self._slaveId = 0
            return False

        if isinstance(msg, GameFightTurnStartMessage):
            gftsmsg = msg
            playerId = PlayedCharacterManager().id
            self._currentPlayerId = gftsmsg.id
            if not self._lastPlayerId:
                self._lastPlayerId = self._currentPlayerId
            logger.info("Start turn for entityId: " + self._currentPlayerId)
            if self._currentPlayerId == playerId:
                self._slaveId = 0
            self._playingSlaveEntity = gftsmsg.id == self._slaveId
            self._turnFrame.turnDuration = gftsmsg.waitTime * 100
            isResumeMessage = msg is GameFightTurnResumeMessage
            if not isResumeMessage:
                BuffManager().decrementDuration(gftsmsg.id)
                BuffManager().resetTriggerCount(gftsmsg.id)
            else:
                currentPlayedFighterId = CurrentPlayedFighterManager().currentFighterId
                nextPlayable = self.getNextPlayableCharacterId()
                if (
                    self._slaveId
                    and self._currentPlayerId != currentPlayedFighterId
                    and (
                        self._slaveId == self._currentPlayerId
                        or nextPlayable == self._slaveId
                    )
                ):
                    self.prepareNextPlayableCharacter(self._masterId)
            if gftsmsg.id > 0 or self._playingSlaveEntity:
                if (
                    fightEntitiesFrame.FightEntitiesFrame.getCurrentInstance().getEntityInfos(
                        gftsmsg.id
                    )
                    and fightEntitiesFrame.FightEntitiesFrame.getCurrentInstance()
                    .getEntityInfos(gftsmsg.id)
                    .disposition.cellId
                    != -1
                    and not FightEntitiesHolder().getEntity(gftsmsg.id)
                ):
                    entity = DofusEntities.getEntity(gftsmsg.id)
                    if entity != None:
                        ss = SerialSequencer()
                        ss.addStep(AddGfxEntityStep(154, entity.position.cellId))
                        ss.start()
                        yOffset = 65 * entity.look.getScaleY()
                        ss2 = SerialSequencer()
                        ss2.addStep(
                            AddGfxEntityStep(153, entity.position.cellId, 0, -yOffset)
                        )
                        ss2.start()
                    self._playerNewTurn = entity
            deadEntityInfo = fightEntitiesFrame.FightEntitiesFrame.getCurrentInstance().getEntityInfos(
                gftsmsg.id
            )
            if (
                (gftsmsg.id == playerId or self._playingSlaveEntity)
                and deadEntityInfo
                and deadEntityInfo.spawnInfo.alive
            ):
                CurrentPlayedFighterManager().currentFighterId = gftsmsg.id
                spellwrapper.SpellWrapper.refreshAllPlayerSpellHolder(gftsmsg.id)
                self._turnFrame.myTurn = True
            else:
                self._turnFrame.myTurn = False
            if self._turnFrame.myTurn and PlayerManager().kisServerPort > 0:
                if ExternalNotificationManager().canAddExternalNotification(
                    ExternalNotificationTypeEnum.KOLO_TURN_START
                ):
                    pass
            if self._skipTurnTimer:
                self._skipTurnTimer.stop()
                self._skipTurnTimer.removeEventListener(
                    TimerEvent.TIMER, self.onSkipTurnTimeOut
                )
                self._skipTurnTimer = None
            if gftsmsg.id == playerId or self._playingSlaveEntity:
                if AFKFightManager().isAfk:
                    fightContextFrame = (
                        krnl.Kernel()
                        .getWorker()
                        .getFrame(fightContextFrame.FightContextFrame)
                    )
                    if fightContextFrame and not fightContextFrame.isKolossium:
                        time = perf_counter()
                        if AFKFightManager().lastTurnSkip + 5 * 1000 < time:
                            action = GameFightTurnFinishAction()
                            krnl.Kernel().getWorker().process(action)
                        else:
                            self._skipTurnTimer = Timer(
                                5 - (time - AFKFightManager().lastTurnSkip),
                                self.onSkipTurnTimeOut,
                            )
                            self._skipTurnTimer.start()
                else:
                    fightEntitesFrame = (
                        krnl.Kernel()
                        .getWorker()
                        .getFrame(fightEntitiesFrame.FightEntitiesFrame)
                    )
                    alivePlayers = 0
                    for en in fightEntitesFrame.entities:
                        if (
                            en is GameFightCharacterInformations
                            and GameFightCharacterInformations(en).spawnInfo.alive
                            and en.contextualId > 0
                        ):
                            alivePlayers += 1
                    if alivePlayers > 0:
                        AFKFightManager().initialize()
            self.removeSavedPosition(gftsmsg.id)
            entitiesFrame = (
                krnl.Kernel()
                .getWorker()
                .getFrame(fightEntitiesFrame.FightEntitiesFrame)
            )
            entitiesIds = entitiesFrame.getEntitiesIdsList()
            numEntities = len(entitiesIds)
            for i in range(numEntities):
                fighterInfos = entitiesFrame.getEntityInfos(entitiesIds[i])
                if fighterInfos and fighterInfos.stats.summoner == gftsmsg.id:
                    self.removeSavedPosition(entitiesIds[i])
            krnl.Kernel().getWorker().getFrame(fightContextFrame.FightContextFrame)
            return True

        if isinstance(msg, GameFightTurnStartPlayingMessage):
            # SpeakingItemManager().triggerEvent(
            #     SpeakingItemManager.SPEAK_TRIGGER_PLAYER_TURN_START
            # )
            return True

        if isinstance(msg, GameFightTurnEndMessage):
            gftemsg = msg
            if not self._confirmTurnEnd:
                self._lastPlayerId = gftemsg.id
            else:
                self._nextLastPlayerId = gftemsg.id
            entityInfos = (
                fightBattleFrame.FightEntitiesFrame.getCurrentInstance().getEntityInfos(
                    gftemsg.id
                )
            )
            if (
                isinstance(entityInfos, GameFightFighterInformations)
                and not entityInfos
            ):
                fighterInfosTE = entityInfos
                BuffManager().markFinishingBuffs(gftemsg.id)
                pass
                if gftemsg.id == CurrentPlayedFighterManager().currentFighterId:
                    CurrentPlayedFighterManager().getSpellCastManager().nextTurn()
                    spellwrapper.SpellWrapper.refreshAllPlayerSpellHolder(gftemsg.id)
            if gftemsg.id == CurrentPlayedFighterManager().currentFighterId:
                AFKFightManager().lastTurnSkip = perf_counter()
                AFKFightManager().confirm = True
                self._turnFrame.myTurn = False
            return True

        if isinstance(msg, SequenceStartMessage):
            self._autoEndTurn = False
            if not self._sequenceFrameSwitcher:
                self._sequenceFrameSwitcher = FightSequenceSwitcherFrame()
                krnl.Kernel().getWorker().addFrame(self._sequenceFrameSwitcher)
            self._currentSequenceFrame = FightSequenceFrame(
                self, self._currentSequenceFrame
            )
            self._sequenceFrameSwitcher.currentFrame = self._currentSequenceFrame
            return True

        if isinstance(msg, SequenceEndMessage):
            semsg = msg
            if not self._currentSequenceFrame:
                logger.warn(
                    "Wow wow wow, I've got a Sequence End but no Sequence Start? What the hell?"
                )
                return True
            self._currentSequenceFrame.mustAck = (
                semsg.authorId == CurrentPlayedFighterManager().currentFighterId
            )
            self._currentSequenceFrame.ackIdent = semsg.actionId
            self._sequenceFrameSwitcher.currentFrame = None
            if not self._currentSequenceFrame.parent:
                krnl.Kernel().getWorker().removeFrame(self._sequenceFrameSwitcher)
                self._sequenceFrameSwitcher = None
                self._sequenceFrames.append(self._currentSequenceFrame)
                self._currentSequenceFrame = None
                self.executeNextSequence()
            else:
                self._currentSequenceFrame.execute()
                self._sequenceFrameSwitcher.currentFrame = (
                    self._currentSequenceFrame.parent
                )
                self._currentSequenceFrame = self._currentSequenceFrame.parent
            return True

        if isinstance(msg, GameFightTurnReadyRequestMessage):
            if self._executingSequence:
                logger.warn(
                    "Delaying turn end acknowledgement because we're still in a sequence."
                )
                self._confirmTurnEnd = True
            else:
                self.confirmTurnEnd()
            return False

        if isinstance(msg, GameFightNewWaveMessage):
            gfnwmsg = msg
            self._newWaveId = gfnwmsg.id
            self._newWave = True
            return True

        if isinstance(msg, GameFightNewRoundMessage):
            gfnrmsg = msg
            self._turnsCount = gfnrmsg.roundNumber
            CurrentPlayedFighterManager().getSpellCastManager().currentTurn = (
                self._turnsCount
            )

            if GameDebugManager().buffsDebugActivated:
                logger.debug(f"[BUFFS DEBUG] Début du tour de jeu {self._turnsCount}!")
            BuffManager().spellBuffsToIgnore = []
            return True

        if isinstance(msg, GameFightLeaveMessage):
            gflmsg = msg
            fighterInfos2 = (
                fightBattleFrame.FightEntitiesFrame.getCurrentInstance().getEntityInfos(
                    self._lastPlayerId
                )
            )
            leaveSequenceFrame = FightSequenceFrame(self)
            if fighterInfos2 and fighterInfos2.spawnInfo.alive:
                fakeDeathMessage = GameActionFightLeaveMessage()
                leaveSequenceFrame.process(
                    fakeDeathMessage.initGameActionFightLeaveMessage(
                        0, 0, gflmsg.charId
                    )
                )
                self._sequenceFrames.append(leaveSequenceFrame)
                self.executeNextSequence()
            if (
                gflmsg.charId == PlayedCharacterManager().id
                and PlayedCharacterManager().isSpectator
            ):
                pass
            return True

        if isinstance(msg, GameFightEndMessage):
            gfemsg = msg
            maxEndRescue = 5
            maxEndRescue -= 1
            while self._currentSequenceFrame and maxEndRescue:
                logger.error("/!\\ Fight end but no SequenceEnd was received")
                seqEnd = SequenceEndMessage()
                seqEnd.init(None, None, None)
                self.process(seqEnd)
                maxEndRescue -= 1
            if self._executingSequence:
                logger.warn("Delaying fight end because we're still in a sequence.")
                self._endBattle = True
                self._battleResults = gfemsg
            else:
                self.endBattle(gfemsg)
            FightersStateManager().endFight()
            CurrentPlayedFighterManager().endFight()
            return True

        if isinstance(msg, GameContextDestroyMessage):
            if self._battleResults:
                logger.debug("Fin de combat propre (resultat connu)")
                self.endBattle(self._battleResults)
            else:
                logger.debug("Fin de combat brutale (pas de resultat connu)")
                self._executingSequence = False
                fakegfemsg = GameFightEndMessage()
                fakegfemsg.init(0, 0, 0, None)
                self.process(fakegfemsg)
            return True

        if isinstance(msg, GameFightPauseMessage):
            gfpmsg = msg
            if gfpmsg.isPaused:
                logger.debug("The fight is paused.")
            else:
                logger.debug("The fight is resuming after pause.")
            self._fightIsPaused = gfpmsg.isPaused
            return True

        if isinstance(msg, DisableAfkAction):
            AFKFightManager().confirm = False
            AFKFightManager().enabled = False
            return True

        if isinstance(msg, UpdateSpellModifierMessage):
            usmmsg = msg
            SpellModifiersManager().setRawSpellModifier(
                usmmsg.actorId, usmmsg.spellModifier
            )
            return True
        else:
            return False

    def pulled(self) -> bool:
        entityId: float = None
        fsf: FightSequenceFrame = None
        self.applyDelayedStats()
        DataMapProvider().isInFight = False
        TweenMax.killAll(False)
        if krnl.Kernel().getWorker().contains(FightTurnFrame):
            krnl.Kernel().getWorker().removeFrame(self._turnFrame)
        BuffManager().destroy()
        MarkedCellsManager().destroy()
        LinkedCellsManager().destroy()
        if self._executingSequence or krnl.Kernel().getWorker().contains(
            FightSequenceFrame
        ):
            logger.warn(
                "Wow, wait. We're pulling FightBattle but there's still sequences inside the worker !!"
            )
            fsf = krnl.Kernel().getWorker().getFrame(FightSequenceFrame)
            krnl.Kernel().getWorker().removeFrame(fsf)
        SerialSequencer.clearByType(FIGHT_SEQUENCER_NAME)
        SerialSequencer.clearByType(FightSequenceFrame.FIGHT_SEQUENCERS_CATEGORY)
        AFKFightManager().enabled = False
        self._currentSequenceFrame = None
        self._sequenceFrameSwitcher = None
        self._turnFrame = None
        self._battleResults = None
        self._newTurnsList = None
        self._newDeadTurnsList = None
        self._turnsList = None
        self._deadTurnsList = None
        self._sequenceFrames = None
        self._playingSlaveEntity = False
        self._masterId = 0
        self._slaveId = 0
        if self._playerNewTurn:
            self._playerNewTurn.destroy()
        if self._skipTurnTimer:
            self._skipTurnTimer.cancel()
            self._skipTurnTimer = None
        self._destroyed = True
        if self._autoEndTurnTimer:
            self._autoEndTurnTimer.removeEventListener(
                TimerEvent.TIMER_COMPLETE, self.sendAutoEndTurn
            )
            self._autoEndTurnTimer = None
        return True

    def delayCharacterStatsList(self, msg: CharacterStatsListMessage) -> None:
        self._delayCslmsg = msg

    def prepareNextPlayableCharacter(self, currentCharacterId: float = 0) -> None:
        nextCharacterEntity: GameFightFighterInformations = None
        nextCharacterId: float = None
        if self._slaveId:
            if currentCharacterId:
                nextCharacterId = (
                    float(self._masterId)
                    if currentCharacterId == self._slaveId
                    else float(self._slaveId)
                )
            else:
                nextCharacterId = self.getNextPlayableCharacterId()
            nextCharacterEntity = (
                fightBattleFrame.FightEntitiesFrame.getCurrentInstance().getEntityInfos(
                    nextCharacterId
                )
            )
            if not nextCharacterEntity or not nextCharacterEntity.spawnInfo.alive:
                return
            CurrentPlayedFighterManager().currentFighterId = nextCharacterId
            if nextCharacterId == self._masterId:
                FightApi.slaveContext = False
                CurrentPlayedFighterManager().resetPlayerSpellList()
                SpellInventoryManagementFrame.getCurrentInstance().applySpellGlobalCoolDownInfo(
                    self._masterId
                )
            elif nextCharacterId == self._slaveId:
                pass

    def getNextPlayableCharacterId(self) -> float:
        masterIdx: int = 0
        slaveIdx: int = 0
        currentCharacterIdx: int = 0
        currentPlayedCharacterId: float = CurrentPlayedFighterManager().currentFighterId
        if not self._slaveId or not self._turnsList:
            return currentPlayedCharacterId
        for i in range(len(self._turnsList)):
            if self._turnsList[i] == self._masterId:
                masterIdx = i
            elif self._turnsList[i] == self._slaveId:
                slaveIdx = i
            if self._turnsList[i] == self._currentPlayerId:
                currentCharacterIdx = i
        if masterIdx == currentCharacterIdx:
            return self._slaveId
        if slaveIdx == currentCharacterIdx:
            return self._masterId
        if masterIdx < currentCharacterIdx and slaveIdx > currentCharacterIdx:
            return self._slaveId
        if masterIdx > currentCharacterIdx and slaveIdx < currentCharacterIdx:
            return self._masterId
        if masterIdx > slaveIdx and masterIdx < currentCharacterIdx:
            return self._slaveId
        if masterIdx < slaveIdx and masterIdx < currentCharacterIdx:
            return self._masterId
        if masterIdx > slaveIdx and masterIdx > currentCharacterIdx:
            return self._slaveId
        if masterIdx < slaveIdx and masterIdx > currentCharacterIdx:
            return self._masterId
        return 0

    def executeNextSequence(self) -> bool:
        if self._executingSequence:
            return False
        nextSequenceFrame: FightSequenceFrame = self._sequenceFrames.pop(0)
        if nextSequenceFrame:
            self._executingSequence = True
            nextSequenceFrame.execute(self.finishSequence(nextSequenceFrame))
            return True
        return False

    def applyDelayedStats(self) -> None:
        if not self._delayCslmsg:
            return
        characterFrame: pcuF.PlayedCharacterUpdatesFrame = (
            krnl.Kernel().getWorker().getFrame(pcuF.PlayedCharacterUpdatesFrame)
        )
        if characterFrame:
            characterFrame.updateCharacterStatsList(self._delayCslmsg.stats)
        self._delayCslmsg = None

    def waitAnimations(self) -> None:
        key = None
        entitiesFrame: fightBattleFrame.FightEntitiesFrame = (
            krnl.Kernel().getWorker().getFrame(fightBattleFrame.FightEntitiesFrame)
        )
        entityIdList: list[float] = None
        if entitiesFrame is not None:
            entityIdList = entitiesFrame.getEntitiesIdsList()
        if entityIdList == None:
            self.sendAcknowledgement()
            return
        maxFramesLeft: float = -1
        for index in range(len(entityIdList)):
            entityId = entityIdList[index]
            tiphonSprite = DofusEntities.getEntity(entityId)
            if tiphonSprite is not None:
                if (
                    tiphonSprite.isPlayingAnimation()
                    and not tiphonSprite.isCurrentAnimationStatic()
                ):
                    if tiphonSprite.framesLeft > maxFramesLeft:
                        maxFramesLeft = tiphonSprite.framesLeft
                        tiphonSpriteToListen = tiphonSprite
        entities: list = EntitiesManager().entities
        for key in entities:
            tiphonSprite = entities[key]
            if tiphonSprite is not None:
                if (
                    tiphonSprite.isPlayingAnimation()
                    and not tiphonSprite.isCurrentAnimationStatic()
                ):
                    if tiphonSprite.framesLeft > maxFramesLeft:
                        maxFramesLeft = tiphonSprite.framesLeft
                        tiphonSpriteToListen = tiphonSprite
        else:
            self.sendAcknowledgement()

    def onLastAnimationFinished(self, tiphonEvent: TiphonEvent = None) -> None:
        tiphonEvent.sprite.removeEventListener(
            TiphonEvent.ANIMATION_END, self.onLastAnimationFinished
        )
        self.sendAcknowledgement()
        if self._confirmTurnEnd:
            self.confirmDelayedTurnEnd()

    def sendAcknowledgement(self) -> None:
        if self._sequenceFrameCached == None:
            return
        ack: GameActionAcknowledgementMessage = GameActionAcknowledgementMessage()
        ack.initGameActionAcknowledgementMessage(
            True, self._sequenceFrameCached.ackIdent
        )
        self._sequenceFrameCached = None
        try:
            ConnectionsHandler.getConnection().send(ack)
        except Exception as e:
            pass

    def finishSequence(self, sequenceFrame: FightSequenceFrame) -> FunctionType:
        def function() -> None:
            if self._destroyed:
                return
            if self.isFightAboutToEnd:
                self.waitAnimations()
            if sequenceFrame.mustAck:
                self._sequenceFrameCached = sequenceFrame
                if not self.isFightAboutToEnd:
                    self.sendAcknowledgement()
            fightEventsHelper.FightEventsHelper.sendAllFightEvent(True)
            logger.info("Sequence finished.")
            self._executingSequence = False
            if self._refreshTurnsList:
                logger.warn(
                    "There was a turns list refresh delayed, what about updating it now?"
                )
                self._refreshTurnsList = False
                self.updateTurnsList(self._newTurnsList, self._newDeadTurnsList)
                self._newTurnsList = None
                self._newDeadTurnsList = None
            if (
                not self._executingSequence
                and len(self._sequenceFrames)
                and self._sequenceFrames[0].instanceId
                >= self._synchroniseFightersInstanceId
            ):
                self.gameFightSynchronize(self._synchroniseFighters)
                self._synchroniseFighters = None
            if self.executeNextSequence():
                self.applyDelayedStats()
                return
            if self._synchroniseFighters:
                self.gameFightSynchronize(self._synchroniseFighters)
                self._synchroniseFighters = None
            self.applyDelayedStats()
            if self._endBattle:
                logger.warn("This fight must end ! Finishing things now.")
                self._endBattle = False
                self.endBattle(self._battleResults)
                self._battleResults = None
                return
            if self._confirmTurnEnd and not self.isFightAboutToEnd:
                self.confirmDelayedTurnEnd()

        return function

    def confirmDelayedTurnEnd(self) -> None:
        logger.warn("There was a turn end delayed, dispatching now.")
        self._confirmTurnEnd = False
        if self._nextLastPlayerId is not None:
            self._lastPlayerId = self._nextLastPlayerId
        self._nextLastPlayerId = None
        self.confirmTurnEnd()

    def sendAutoEndTurn(self, e) -> None:
        action: Action = None
        if self._autoEndTurn:
            action = GameFightTurnFinishAction()
            krnl.Kernel().getWorker().process(action)
            self._autoEndTurn = False
        self._autoEndTurnTimer.stop()

    def updateTurnsList(
        self, turnsList: list[float], deadTurnsList: list[float]
    ) -> None:
        self._turnsList = turnsList
        self._deadTurnsList = deadTurnsList
        pass
        if Dofus().options.getOption(
            "orderFighters"
        ) and krnl.Kernel().getWorker().getFrame(fightBattleFrame.FightEntitiesFrame):
            krnl.Kernel().getWorker().getFrame(fightBattleFrame.FightEntitiesFrame)

    def confirmTurnEnd(self) -> None:
        fighterInfos: GameFightFighterInformations = (
            fightBattleFrame.FightEntitiesFrame.getCurrentInstance().getEntityInfos(
                self._lastPlayerId
            )
        )
        if fighterInfos:
            BuffManager().markFinishingBuffs(self._lastPlayerId)
            if self._lastPlayerId == CurrentPlayedFighterManager().currentFighterId:
                spellwrapper.SpellWrapper.refreshAllPlayerSpellHolder(
                    self._lastPlayerId
                )
                self._playerTargetedEntitiesList = []
                self.prepareNextPlayableCharacter(self._lastPlayerId)
        spellCastManager: SpellCastInFightManager = (
            CurrentPlayedFighterManager().getSpellCastManagerById(self._lastPlayerId)
        )
        if spellCastManager is not None:
            spellCastManager.nextTurn()
        turnEnd: GameFightTurnReadyMessage = GameFightTurnReadyMessage()
        turnEnd.init(True)
        ConnectionsHandler.getConnection().send(turnEnd)

    def endBattle(self, fightEnd: GameFightEndMessage) -> None:
        EntitiesManager().cleanDeadLook()
        _holder: FightEntitiesHolder = FightEntitiesHolder()
        entities: dict = _holder.getEntities()
        for coward in entities:
            coward
        _holder.reset()
        self._synchroniseFighters = None
        krnl.Kernel().getWorker().removeFrame(self)
        fightContextFrame = (
            krnl.Kernel().getWorker().getFrame(fightContextFrame.FightContextFrame)
        )
        fightContextFrame.process(fightEnd)

    def onSkipTurnTimeOut(self, event: TimerEvent) -> None:
        action: Action = None
        self._skipTurnTimer.removeEventListener(
            TimerEvent.TIMER, self.onSkipTurnTimeOut
        )
        self._skipTurnTimer = None
        fightContextFrame = (
            krnl.Kernel().getWorker().getFrame(fightContextFrame.FightContextFrame)
        )
        if AFKFightManager().isAfk and (
            fightContextFrame and not fightContextFrame.isKolossium
        ):
            action = GameFightTurnFinishAction()
            krnl.Kernel().getWorker().process(action)

    def gameFightSynchronize(
        self, fighters: list[GameFightFighterInformations]
    ) -> None:
        newWaveAppeared: bool = False
        newWaveMonster: bool = False
        entitiesFrame: fightBattleFrame.FightEntitiesFrame = (
            krnl.Kernel().getWorker().getFrame(fightBattleFrame.FightEntitiesFrame)
        )
        newWaveMonsterIndex: int = 0
        BuffManager().synchronize()
        for fighterInfos in fighters:
            stats = StatsManager().getStats(fighterInfos.contextualId)
            if fighterInfos.spawnInfo.alive:
                newWaveMonster = (
                    fighterInfos.wave == self._newWaveId
                    and fighterInfos.wave != 0
                    and not DofusEntities.getEntity(fighterInfos.contextualId)
                )
                entitiesFrame.updateFighter(fighterInfos, None)
                BuffManager().markFinishingBuffs(fighterInfos.contextualId, False)
                for buff in BuffManager().getAllBuff(fighterInfos.contextualId):
                    if isinstance(buff, StatBuff):
                        buff.isRecent = False
                if newWaveMonster:
                    newWaveAppeared = True
                    DofusEntities.getEntity(fighterInfos.contextualId).visible = False
                    sequencer = SerialSequencer()
                    sequencer.addStep(WaitStep(0.3 * newWaveMonsterIndex))
                    sequencer.addStep(
                        AddGfxEntityStep(2715, fighterInfos.disposition.cellId)
                    )
                    sequencer.addStep(
                        FightVisibilityStep(fighterInfos.contextualId, True)
                    )
                    sequencer.start()
                    newWaveMonsterIndex += 1
        if newWaveAppeared:
            self._newWave = False
            self._newWaveId = -1
        if self._neverSynchronizedBefore:
            pass
            self._neverSynchronizedBefore = False

    def removeSavedPosition(self, pEntityId: float) -> None:
        fightContextFrame = (
            krnl.Kernel().getWorker().getFrame(fightContextFrame.FightContextFrame)
        )
        savedPositions: list = fightContextFrame.fightersPositionsHistory[pEntityId]
        if savedPositions:
            nbPos = len(savedPositions)
            for i in range(nbPos):
                savedPos = savedPositions[i]
                savedPos.lives -= 1
                if savedPos.lives == 0:
                    del savedPositions[i]
                    i -= 1
                    nbPos -= 1

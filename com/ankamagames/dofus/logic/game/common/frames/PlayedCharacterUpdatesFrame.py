from datetime import datetime
from logging import Logger
from time import perf_counter
from com.ankamagames.dofus.datacenter.world.SubArea import SubArea
import com.ankamagames.dofus.internalDatacenter.spells.SpellWrapper as spellWrapper
from com.ankamagames.dofus.internalDatacenter.stats.EntityStats import EntityStats
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.logic.game.common.managers.InventoryManager import (
    InventoryManager,
)
import com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager as pcm
from com.ankamagames.dofus.logic.game.common.managers.TimerManager import TimeManager
from com.ankamagames.dofus.logic.game.common.misc.DofusEntities import DofusEntities
from com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import (
    CurrentPlayedFighterManager,
)
from com.ankamagames.dofus.logic.game.fight.managers.SpellModifiersManager import (
    SpellModifiersManager,
)
import com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayContextFrame as rplCF
from com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayEntitiesFrame import (
    RoleplayEntitiesFrame,
)
from com.ankamagames.dofus.network.enums.CompassTypeEnum import CompassTypeEnum
from com.ankamagames.dofus.network.enums.PlayerLifeStatusEnum import (
    PlayerLifeStatusEnum,
)
from com.ankamagames.dofus.network.enums.ProtocolConstantsEnum import (
    ProtocolConstantsEnum,
)
from com.ankamagames.dofus.network.enums.StatsUpgradeResultEnum import (
    StatsUpgradeResultEnum,
)
from com.ankamagames.dofus.network.enums.GameServerTypeEnum import GameServerTypeEnum
from com.ankamagames.dofus.network.messages.game.almanach.AlmanachCalendarDateMessage import (
    AlmanachCalendarDateMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassResetMessage import (
    CompassResetMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import (
    CompassUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdatePartyMemberMessage import (
    CompassUpdatePartyMemberMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdatePvpSeekMessage import (
    CompassUpdatePvpSeekMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicTimeMessage import (
    BasicTimeMessage,
)
from com.ankamagames.dofus.network.messages.game.character.debt.DebtsDeleteMessage import (
    DebtsDeleteMessage,
)
from com.ankamagames.dofus.network.messages.game.character.debt.DebtsUpdateMessage import (
    DebtsUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.character.spell.forgettable.ForgettableSpellDeleteMessage import (
    ForgettableSpellDeleteMessage,
)
from com.ankamagames.dofus.network.messages.game.character.spell.forgettable.ForgettableSpellEquipmentSlotsMessage import (
    ForgettableSpellEquipmentSlotsMessage,
)
from com.ankamagames.dofus.network.messages.game.character.spell.forgettable.ForgettableSpellListUpdateMessage import (
    ForgettableSpellListUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterExperienceGainMessage import (
    CharacterExperienceGainMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpInformationMessage import (
    CharacterLevelUpInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpMessage import (
    CharacterLevelUpMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterStatsListMessage import (
    CharacterStatsListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapSpeedMovementMessage import (
    GameMapSpeedMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import (
    MapComplementaryInformationsDataMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.death.GameRolePlayGameOverMessage import (
    GameRolePlayGameOverMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.death.GameRolePlayPlayerLifeStatusMessage import (
    GameRolePlayPlayerLifeStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.stats.StatsUpgradeResultMessage import (
    StatsUpgradeResultMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.CharacterCapabilitiesMessage import (
    CharacterCapabilitiesMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.ServerExperienceModificatorMessage import (
    ServerExperienceModificatorMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.SetCharacterRestrictionsMessage import (
    SetCharacterRestrictionsMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.zaap.KnownZaapListMessage import (
    KnownZaapListMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMoneyMovementInformationMessage import (
    ExchangeMoneyMovementInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.SetUpdateMessage import (
    SetUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.startup.StartupActionAddMessage import (
    StartupActionAddMessage,
)
from com.ankamagames.dofus.network.messages.game.startup.StartupActionFinishedMessage import (
    StartupActionFinishedMessage,
)
from com.ankamagames.dofus.network.messages.game.startup.StartupActionsListMessage import (
    StartupActionsListMessage,
)
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import (
    CharacterCharacteristicsInformations,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOptionAlliance import (
    HumanOptionAlliance,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOptionOrnament import (
    HumanOptionOrnament,
)
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.enums.Priority import Priority
from damageCalculation.tools import StatIds

logger = Logger(__name__)


class PlayedCharacterUpdatesFrame(Frame):

    SPELL_TOOLTIP_CACHE_NUM: int = 0

    FORGETTABLE_SPELL_FIRST_NOTIF_NAME: str = "firstForgettableSpell"

    setList: list

    guildEmblemSymbolCategories: int

    _kamasLimit: float

    _giftListInitialized: bool

    def __init__(self):
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.HIGH

    @property
    def roleplayContextFrame(self) -> rplCF.RoleplayContextFrame:
        return krnl.Kernel().getWorker().getFrame(rplCF.RoleplayContextFrame)

    @property
    def kamasLimit(self) -> float:
        return self._kamasLimit

    def pushed(self) -> bool:
        self.setList = []
        self._giftListInitialized = False
        return True

    def process(self, msg: Message) -> bool:

        if isinstance(msg, SetCharacterRestrictionsMessage):
            scrmsg = msg
            if scrmsg.actorId == pcm.PlayedCharacterManager().id:
                pcm.PlayedCharacterManager().restrictions = scrmsg.restrictions
            rpEntitiesFrame = krnl.Kernel().getWorker().getFrame(RoleplayEntitiesFrame)
            if rpEntitiesFrame:
                infos = rpEntitiesFrame.getEntityInfos(scrmsg.actorId)
                if infos and infos.humanoidInfo:
                    infos.humanoidInfo.restrictions = scrmsg.restrictions
            return False

        if isinstance(msg, ServerExperienceModificatorMessage):
            semsg = msg
            pcm.PlayedCharacterManager().experiencePercent = (
                semsg.experiencePercent - 100
            )
            return True

        if isinstance(msg, CharacterStatsListMessage):
            # cslmsg = msg
            # fightBattleFrame = krnl.Kernel().getWorker().getFrame(FightBattleFrame)
            # if fightBattleFrame is not None and fightBattleFrame.executingSequence:
            #    fightBattleFrame.delayCharacterStatsList(cslmsg)
            # else:
            #    self.updateCharacterStatsList(cslmsg.stats)
            # if self.roleplayContextFrame and self.roleplayContextFrame.entitiesFrame:
            #    playerInfos = self.roleplayContextFrame.entitiesFrame.getEntityInfos(pcm.PlayedCharacterManager().id)
            #    if playerInfos:
            #       playerInfos.alignmentInfos = cslmsg.stats.alignmentInfos
            # if krnl.Kernel().getWorker().getFrame(QuestFrame).achievmentsListProcessed == False:
            #    krnl.Kernel().getWorker().getFrame(QuestFrame)
            return True

        if isinstance(msg, MapComplementaryInformationsDataMessage):
            mcidmsg = msg
            for grai in mcidmsg.actors:
                grpci = grai
                if grpci and grpci.contextualId == pcm.PlayedCharacterManager().id:
                    pcm.PlayedCharacterManager().infos.entityLook = grpci.look
                    for opt in grpci.humanoidInfo.options:
                        if isinstance(opt, HumanOptionAlliance):
                            pcm.PlayedCharacterManager().characteristics.alignmentInfos.aggressable = (
                                opt.aggressable
                            )

            # if not (pcm.PlayedCharacterManager().characteristics.alignmentInfos.aggressable == AggressableStatusEnum.AvA_DISQUALIFIED or\
            #     pcm.PlayedCharacterManager().characteristics.alignmentInfos.aggressable == AggressableStatusEnum.AvA_ENABLED_AGGRESSABLE or\
            #         pcm.PlayedCharacterManager().characteristics.alignmentInfos.aggressable == AggressableStatusEnum.AvA_ENABLED_NON_AGGRESSABLE or\
            #             pcm.PlayedCharacterManager().characteristics.alignmentInfos.aggressable == AggressableStatusEnum.AvA_PREQUALIFIED_AGGRESSABLE):
            #    return False

            newSubArea = SubArea.getSubAreaByMapId(mcidmsg.mapId)

            # if pcm.PlayedCharacterManager().currentSubArea and newSubArea:
            #    if PrismSubAreaWrapper.prismList[newSubArea.id]:
            #       prism = PrismSubAreaWrapper.prismList[newSubArea.id]
            #       if prism.state == PrismStateEnum.PRISM_STATE_VULNERABLE:
            #          if krnl.Kernel().getWorker().contains(AllianceFrame):
            #             allianceFrame = krnl.Kernel().getWorker().getFrame(AllianceFrame)

            return False

        if isinstance(msg, CharacterCapabilitiesMessage):
            ccmsg = msg
            self.guildEmblemSymbolCategories = ccmsg.guildEmblemSymbolCategories
            return True

        # if isinstance(msg, ResetCharacterStatsRequestAction):
        #    rcsra = msg
        #    rcsrmsg = ResetCharacterStatsRequestMessage()
        #    rcsrmsg.initResetCharacterStatsRequestMessage()
        #    ConnectionsHandler.getConnection().send(rcsrmsg)
        #    return True

        # if isinstance(msg, StatsUpgradeRequestAction):
        #    sura = msg
        #    surqmsg = StatsUpgradeRequestMessage()
        #    surqmsg.initStatsUpgradeRequestMessage(sura.useAdditionnal,sura.statId,sura.boostPoint)
        #    ConnectionsHandler.getConnection().send(surqmsg)
        #    return True

        if isinstance(msg, StatsUpgradeResultMessage):
            surmsg = msg
            if surmsg.result == StatsUpgradeResultEnum.SUCCESS:
                pass
            return True

        if isinstance(msg, CharacterLevelUpMessage):
            clumsg = msg
            messageId = clumsg.getMessageId()
            if messageId == CharacterLevelUpMessage.protocolId:
                previousLevel = pcm.PlayedCharacterManager().infos.level
                pcm.PlayedCharacterManager().infos.level = clumsg.newLevel
                if (
                    clumsg.newLevel == 10
                    and PlayerManager().server.gameTypeId
                    != GameServerTypeEnum.SERVER_TYPE_TEMPORIS
                ):
                    InventoryManagementFrame.displayNewsPopupClassic()
                caracPointEarned = 0
                healPointEarned = 0
                caracPointEarned = (clumsg.newLevel - previousLevel) * 5
                healPointEarned = (clumsg.newLevel - previousLevel) * 5
                newSpellWrappers = []
                playerBreed = Breed.getBreedById(
                    pcm.PlayedCharacterManager().infos.breed
                )
                for spellVariant in playerBreed.breedSpellVariants:
                    for spellBreed in spellVariant.spells:
                        for spellLevelBreedId in spellBreed.spellLevels:
                            spellLevelBreed = SpellLevel.getLevelById(spellLevelBreedId)
                            if spellLevelBreed:
                                obtentionLevel = spellLevelBreed.minPlayerLevel
                                if (
                                    obtentionLevel <= clumsg.newLevel
                                    and obtentionLevel > previousLevel
                                ):
                                    newSpellWrappers.append(
                                        spellWrapper.SpellWrapper.create(
                                            spellBreed.id, spellLevelBreed.grade, False
                                        )
                                    )
                for spellWrapper in pcm.PlayedCharacterManager().spellsInventory:
                    spellWrapper.updateSpellLevelAndEffectsAccordingToPlayerLevel()
                if len(newSpellWrappers):
                    # new level handle
                    pass
                try:
                    pass
                except Exception as e:
                    pass
                if self.roleplayContextFrame:
                    entityInfos = (
                        self.roleplayContextFrame.entitiesFrame.getEntityInfos(
                            pcm.PlayedCharacterManager().id
                        )
                    )
                if entityInfos:
                    for option in entityInfos.humanoidInfo.options:
                        if isinstance(option, HumanOptionOrnament):
                            option.level = clumsg.newLevel
            if messageId == CharacterLevelUpInformationMessage.protocolId:
                cluimsg = msg
                onSameMap = False
                try:
                    for (
                        entityId
                    ) in self.roleplayContextFrame.entitiesFrame.getEntitiesIdsList():
                        if entityId == cluimsg.id:
                            onSameMap = True
                    if onSameMap:
                        pass
                except Exception as e:
                    logger.warn(
                        "Un probl�me est survenu lors du traitement du message CharacterLevelUpInformationMessage. "
                        + "Un personnage vient de changer de niveau mais on n'est surement pas encore sur la map"
                    )
                if cluimsg.newLevel <= ProtocolConstantsEnum.MAX_LEVEL:
                    pass
            return False

        if isinstance(msg, CharacterExperienceGainMessage):
            cegmsg = msg
            return True

        if isinstance(msg, GameRolePlayPlayerLifeStatusMessage):
            grplsmsg = msg
            pcm.PlayedCharacterManager().state = grplsmsg.state
            return True

        if isinstance(msg, GameRolePlayGameOverMessage):
            grpgomsg = msg
            pcm.PlayedCharacterManager().state = PlayerLifeStatusEnum.STATUS_TOMBSTONE
            return True

        if isinstance(msg, AlmanachCalendarDateMessage):
            # acdmsg = msg
            # AlmanaxManager().calendar = AlmanaxCalendar.getAlmanaxCalendarById(acdmsg.date)
            return True

        if isinstance(msg, SetUpdateMessage):
            # sumsg = msg
            # self.setList[sumsg.setId] = PlayerSetInfo(sumsg.setId, sumsg.setObjects, sumsg.setEffects)
            return True

        if isinstance(msg, CompassResetMessage):
            # crmsg = msg
            # name = "flag_srv" + crmsg.type

            # if crmsg.type  == CompassTypeEnum.COMPASS_TYPE_SPOUSE:
            #    socialFrame = krnl.Kernel().getWorker().getFrame(SocialFrame)
            #    socialFrame.spouse.followSpouse = False

            # if crmsg.type  == CompassTypeEnum.COMPASS_TYPE_PARTY:
            #    pcm.PlayedCharacterManager().followingPlayerIds = []
            #    return True
            return True

        if isinstance(msg, CompassUpdatePartyMemberMessage):
            pass

        if isinstance(msg, CompassUpdatePvpSeekMessage):
            pass

        if isinstance(msg, CompassUpdateMessage):
            cumsg = msg
            name = "flag_srv" + cumsg.type
            if cumsg.type == CompassTypeEnum.COMPASS_TYPE_PARTY:
                memberId = CompassUpdatePartyMemberMessage(msg).memberId
                active = CompassUpdatePartyMemberMessage(msg).active
                if memberId == 0 and not active:
                    for (
                        followingPlayerId
                    ) in pcm.PlayedCharacterManager().followingPlayerIds:
                        pass
                    pcm.PlayedCharacterManager().followingPlayerIds = []
                else:
                    pmFrame = krnl.Kernel().getWorker().getFrame(PartyManagementFrame)
                    if pmFrame:
                        memberInfo = pmFrame.getGroupMemberById(memberId)
                        if memberInfo:
                            pass
                        name += "_" + memberId
                    if active:
                        pass
                    else:
                        pass
                return True
            if cumsg.type == CompassTypeEnum.COMPASS_TYPE_PVP_SEEK:
                legend = (
                    I18n.getUiText(
                        "ui.cartography.positionof",
                        [CompassUpdatePvpSeekMessage(msg).memberName],
                    )
                    + " ("
                    + CompassUpdatePvpSeekMessage(msg).coords.worldX
                    + ","
                    + CompassUpdatePvpSeekMessage(msg).coords.worldY
                    + ")"
                )

            if cumsg.type == CompassTypeEnum.COMPASS_TYPE_QUEST:
                legend = cumsg.coords.worldX + "," + cumsg.coords.worldY

            if cumsg.type == CompassTypeEnum.COMPASS_TYPE_SIMPLE:
                legend = cumsg.coords.worldX + "," + cumsg.coords.worldY

            if cumsg.type == CompassTypeEnum.COMPASS_TYPE_SPOUSE:
                socialFrame2 = krnl.Kernel().getWorker().getFrame(SocialFrame)
                socialFrame2.spouse.followSpouse = True
            return True

        if isinstance(msg, BasicTimeMessage):
            btmsg = msg
            receptionDelay = perf_counter() - btmsg.receptionTime
            TimeManager().serverTimeLag = (
                btmsg.timestamp
                + btmsg.timezoneOffset * 60 * 1000
                - datetime.now().timestamp()
                + receptionDelay
            )
            TimeManager().serverUtcTimeLag = (
                btmsg.timestamp - datetime.now().timestamp() + receptionDelay
            )
            return True

        if isinstance(msg, StartupActionsListMessage):
            # salm = msg
            # giftList = []
            # initialGiftCount = 0
            # if pcm.PlayedCharacterManager().waitingGifts and pcm.PlayedCharacterManager().len(waitingGifts) != 0:
            #    initialGiftCount = pcm.PlayedCharacterManager().len(waitingGifts)
            # for gift in salm.actions:
            #        _items = []
            #    for item in gift.items:
            #       iw = ItemWrapper.create(0,0,item.objectGID,item.quantity,item.effects,False)
            #       _items.append(iw)
            #       obj = {
            #          "uid":gift.uid,
            #          "title":gift.title,
            #          "text":gift.text,
            #          "items":_items
            #       }
            #    giftList.append(obj)
            # pcm.PlayedCharacterManager().waitingGifts = giftList
            # if len(giftList) > 0:
            #    if self._giftListInitialized and len(giftList) != initialGiftCount and len(giftList) > initialGiftCount:
            #       pass
            # self._giftListInitialized = True
            return True

        if isinstance(msg, StartupActionAddMessage):
            # saam = msg
            # items = []
            # for itema in saam.newAction.items:
            #    iw = ItemWrapper.create(0,0,itema.objectGID,itema.quantity,itema.effects,False)
            #    items.append(iw)
            # obj = {
            #    "uid":saam.newAction.uid,
            #    "title":saam.newAction.title,
            #    "text":saam.newAction.text,
            #    "items":items
            # }
            # pcm.PlayedCharacterManager().waitingGifts.append(obj)
            return True

        # if isinstance(msg, GiftAssignRequestAction):
        #    gar = msg
        #    sao = StartupActionsObjetAttributionMessage()
        #    sao.initStartupActionsObjetAttributionMessage(gar.giftId,gar.characterId)
        #    ConnectionsHandler.getConnection().send(sao)
        #    return True

        # if isinstance(msg, GiftAssignAllRequestAction):
        #    gaara = msg
        #    saaamsg = StartupActionsAllAttributionMessage()
        #    saaamsg.initStartupActionsAllAttributionMessage(gaara.characterId)
        #    ConnectionsHandler.getConnection().send(saaamsg)
        #    return True

        if isinstance(msg, StartupActionFinishedMessage):
            # safm = msg
            # indexToDelete = -1
            # for giftAction in pcm.PlayedCharacterManager().waitingGifts:
            #    if giftAction.uid == safm.actionId:
            #       indexToDelete = pcm.PlayedCharacterManager().waitingGifts.find(giftAction)
            # if indexToDelete > -1:
            #    pcm.PlayedCharacterManager().waitingGifts.splice(indexToDelete,1)
            #    if len(pcm.PlayedCharacterManager().waitingGifts) == 0:
            #       pass
            return True

        if isinstance(msg, ExchangeMoneyMovementInformationMessage):
            emmim = msg
            self._kamasLimit = emmim.limit
            return True

        if isinstance(msg, DebtsUpdateMessage):
            dum = msg
            # DebtManager().updateDebts(dum.debts)
            return True

        if isinstance(msg, DebtsDeleteMessage):
            ddm = msg
            # DebtManager().removeDebts(ddm.debts)
            return True

        if isinstance(msg, ForgettableSpellListUpdateMessage):
            # fslumsg = msg
            # if fslumsg.action == ForgettableSpellListActionEnum.FORGETTABLE_SPELL_LIST_DISPATCH:
            #    newSpellList = dict()
            #    for forgettableSpell in fslumsg.spells:
            #       newSpellList[forgettableSpell.spellId] = forgettableSpell
            #    pcm.PlayedCharacterManager().playerForgettableSpelldict = newSpellList
            # else:
            #    ds = DataStoreType("AccountModule_",True,DataStoreEnum.LOCATION_LOCAL,DataStoreEnum.BIND_ACCOUNT)
            #    if not StoreDataManager().getData(ds,FORGETTABLE_SPELL_FIRST_NOTIF_NAME):
            #       StoreDataManager().setData(ds,FORGETTABLE_SPELL_FIRST_NOTIF_NAME,True)
            #       nid = NotificationManager().prepareNotification(I18n.getUiText("ui.temporis.popupFirstSpellAddedTitle"),I18n.getUiText("ui.temporis.popupFirstSpellAddedContent"),NotificationTypeEnum.TUTORIAL,"FirstForgettableSpellNotif")
            #       NotificationManager().addButtonToNotification(nid,I18n.getUiText("ui.temporis.popupFirstSpellAddedButton"),"OpenForgettableSpellsUiAction")
            #       NotificationManager().sendNotification(nid)
            #    playerForgettableSpellsDict = pcm.PlayedCharacterManager().playerForgettableSpelldict
            #    for forgettableSpell in fslumsg.spells:
            #       playerForgettableSpellsDict[forgettableSpell.spellId] = forgettableSpell
            # KernelEventsManager().processCallback(HookList.ForgettableSpellListUpdate)
            # StorageOptionManager().updateStorageView()
            # InventoryManager().inventory.releaseHooks()
            return True

        if isinstance(msg, ForgettableSpellDeleteMessage):
            # fsdmsg = msg
            # playerForgettableSpellsDict = pcm.PlayedCharacterManager().playerForgettableSpelldict
            # for forgettableSpellId in fsdmsg.spells:
            #    del playerForgettableSpellsDict[forgettableSpellId]
            # StorageOptionManager().updateStorageView()
            # InventoryManager().inventory.releaseHooks()
            return True

        if isinstance(msg, ForgettableSpellEquipmentSlotsMessage):
            # fsesmsg = msg
            # pcm.PlayedCharacterManager().playerMaxForgettableSpellsfloat = fsesmsg.quantity
            return True

        if isinstance(msg, KnownZaapListMessage):
            kzlmsg = msg
            pcm.PlayedCharacterManager().updateKnownZaaps(kzlmsg.destinations)
            return True

        # if isinstance(msg, UpdateSpellModifierAction):
        #    usmaction = msg
        #    self.updateSpellModifier(usmaction.entityId,usmaction.spellId,usmaction.statId)
        #    return True

        if isinstance(msg, GameMapSpeedMovementMessage):
            gmsmm = msg
            newSpeedAjust = 10 * (gmsmm.speedMultiplier - 1)
            pcm.PlayedCharacterManager().speedAjust = newSpeedAjust
            if (
                DofusEntities.getEntity(pcm.PlayedCharacterManager().id) is not None
                and self.roleplayContextFrame is not None
            ):
                DofusEntities.getEntity(
                    pcm.PlayedCharacterManager().id
                ).speedAdjust = newSpeedAjust
            return True

        return False

    def updateCharacterStatsList(
        self, stats: CharacterCharacteristicsInformations
    ) -> None:
        playerId: float = pcm.PlayedCharacterManager().id
        statsManager: StatsManager = StatsManager()
        playerStats: EntityStats = statsManager.getStats(playerId)
        if playerStats is not None:
            oldEnergyPoints = playerStats.getStatTotalValue(StatIds.ENERGY_POINTS)
        statsManager.addRawStats(playerId, stats.characteristics)
        SpellModifiersManager().setRawSpellsModifiers(
            playerId, stats.spellModifications
        )
        if stats.kamas != InventoryManager().inventory.kamas:
            InventoryManager().inventory.kamas = stats.kamas
        pcm.PlayedCharacterManager().characteristics = stats
        if pcm.PlayedCharacterManager().isFighting:
            if CurrentPlayedFighterManager().isRealPlayer():
                pass
            spellWrapper.SpellWrapper.refreshAllPlayerSpellHolder(pcm.PlayedCharacterManager().id)
        else:
            pass

    def updateSpellModifier(
        self, targetId: float, spellId: float, statId: float
    ) -> None:
        playerId: float = pcm.PlayedCharacterManager().id
        if playerId is not targetId:
            return
        spell = spellWrapper.SpellWrapper.getSpellWrapperById(spellId, playerId)
        if spell is not None:
            spell = spell.clone()
            ++spell.versionNum

    def pulled(self) -> bool:
        return True

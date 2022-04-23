from com.ankamagames.berilia.interfaces.IApi import IApi
from com.ankamagames.dofus.datacenter.breeds.Breed import Breed
from com.ankamagames.dofus.datacenter.optionalFeatures.ForgettableSpell import (
    ForgettableSpell,
)
from com.ankamagames.dofus.datacenter.world.SubArea import SubArea
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.internalDatacenter.items.WeaponWrapper import WeaponWrapper
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.dofus.internalDatacenter.items.IdolsPresetWrapper import (
        IdolsPresetWrapper,
    )
    from com.ankamagames.dofus.internalDatacenter.spells.SpellWrapper import (
        SpellWrapper,
    )
from com.ankamagames.dofus.internalDatacenter.mount.MountData import MountData
from com.ankamagames.dofus.internalDatacenter.stats.EntityStats import EntityStats
from com.ankamagames.dofus.internalDatacenter.world.WorldPointWrapper import (
    WorldPointWrapper,
)
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.logic.game.common.frames.AbstractEntitiesFrame import (
    AbstractEntitiesFrame,
)
import com.ankamagames.dofus.logic.game.common.frames.PlayedCharacterUpdatesFrame as pcuF
from com.ankamagames.dofus.logic.game.common.managers.InventoryManager import (
    InventoryManager,
)
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.fight.frames.FightPreparationFrame import (
    FightPreparationFrame,
)
from com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager import (
    CurrentPlayedFighterManager,
)
from com.ankamagames.dofus.logic.game.fight.types.castSpellManager.SpellManager import (
    SpellManager,
)
from com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayContextFrame import (
    RoleplayContextFrame,
)
from com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayEntitiesFrame import (
    RoleplayEntitiesFrame,
)
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import (
    CharacterInventoryPositionEnum,
)
from com.ankamagames.dofus.network.enums.PlayerLifeStatusEnum import (
    PlayerLifeStatusEnum,
)
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import (
    CharacterCharacteristicsInformations,
)
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import (
    CharacterBaseInformations,
)
from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import (
    ActorRestrictionsInformations,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import (
    GameRolePlayActorInformations,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayCharacterInformations import (
    GameRolePlayCharacterInformations,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayMutantInformations import (
    GameRolePlayMutantInformations,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import (
    GuildInformations,
)
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOptionTitle import (
    HumanOptionTitle,
)
from com.ankamagames.dofus.network.types.game.data.items.ForgettableSpellItem import (
    ForgettableSpellItem,
)
from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import (
    GuildApplicationInformation,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton

logger = Logger(__name__)


class PlayedCharacterApi(IApi, metaclass=Singleton):

    MEMORY_LOG: dict = dict()

    def __init__(self):
        super().__init__()

    def characteristics(self) -> CharacterCharacteristicsInformations:
        return PlayedCharacterManager().characteristics

    def stats(self) -> EntityStats:
        return StatsManager().getStats(PlayedCharacterManager().id)

    def getPlayedCharacterInfo(self) -> object:
        i: CharacterBaseInformations = PlayedCharacterManager().infos
        if not i:
            return None

        class o:
            pass

        o.id = i.id
        o.breed = i.breed
        o.level = i.level
        o.limitedLevel = PlayedCharacterManager().limitedLevel
        o.sex = i.sex
        o.name = i.name
        return o

    # def getCurrentEntityLook(self) -> TiphonEntityLook:
    #    look:TiphonEntityLook = None
    #    entity:AnimatedCharacter = DofusEntities.getEntity(PlayedCharacterManager().id) as AnimatedCharacter
    #    if entity:
    #       look = entity.look.clone()
    #    else:
    #       look = EntityLookAdapter.fromNetwork(PlayedCharacterManager().infos.entityLook)
    #    return look

    def getInventory(self) -> list[ItemWrapper]:
        return InventoryManager().realInventory

    def getEquipment(self) -> list:
        item = None
        equipment: list = list()
        for item in PlayedCharacterManager().inventory:
            if (
                item.position
                <= CharacterInventoryPositionEnum.ACCESSORY_POSITION_SHIELD
            ):
                equipment.append(item)
        return equipment

    def getSpellInventory(self) -> list:
        return PlayedCharacterManager().spellsInventory

    def getSpells(self, returnBreedSpells: bool) -> list:
        spim: SpellInventoryManagementFrame = (
            Kernel().getWorker().getFrame(SpellInventoryManagementFrame)
        )
        if returnBreedSpells:
            return spim.getBreedSpellsInVariantslist()
        return spim.getCommonSpellsInVariantslist()

    def getPlayerForgettableSpells(self) -> dict:
        return PlayedCharacterManager().playerForgettableSpelldict

    def getPlayerMaxForgettableSpellsNumber(self) -> int:
        return PlayedCharacterManager().playerMaxForgettableSpellsNumber

    def getForgettableSpells(self) -> list:
        return ForgettableSpell.getForgettableSpells()

    def getForgettableSpellById(self, id: int) -> ForgettableSpell:
        return ForgettableSpell.getForgettableSpellById(id)

    def isForgettableSpellAvailable(self, id: int) -> bool:
        forgettableSpellItems: dict = (
            PlayedCharacterManager().playerForgettableSpelldict
        )
        if forgettableSpellItems == None:
            return False
        forgettableSpellItem: ForgettableSpellItem = forgettableSpellItems[id]
        if forgettableSpellItem == None:
            return False
        return forgettableSpellItem.available

    def isForgettableSpell(self, spellId: int) -> bool:
        return SpellManager.isForgettableSpell(spellId)

    def getCustomModeBreedSpellById(self, id: int) -> CustomModeBreedSpell:
        return CustomModeBreedSpell.getCustomModeBreedSpellById(id)

    def getCustomModeSpellIds(self) -> list:
        return CustomModeBreedSpell.getAllCustomModeBreedSpellIds()

    def getCustomModeBreedSpellList(self, breedId: int) -> list:
        return CustomModeBreedSpell.getCustomModeBreedSpellList(breedId)

    def getBreedSpellActivatedIds(self) -> list:
        spellsInventory: list = PlayedCharacterManager().spellsInventory
        activatedSpellIds: list = list()
        playerBreedId: int = PlayedCharacterManager().infos.breed
        breedData: Breed = Breed.getBreedById(playerBreedId)
        breedSpellsId: list = breedData.allSpellsId
        for spellWrapper in spellsInventory:
            if spellWrapper is not None:
                if (
                    spellWrapper.variantActivated
                    and breedSpellsId.find(spellWrapper.id) != -1
                ):
                    activatedSpellIds.append(spellWrapper.id)
        return activatedSpellIds

    def getMount(self) -> MountData:
        return PlayedCharacterManager().mount

    def getPetsMount(self) -> ItemWrapper:
        return PlayedCharacterManager().petsMount

    def getTitle(self) -> Title:
        title: Title = None
        playerInfo: GameRolePlayCharacterInformations = None
        option = None
        title2: Title = None
        titleId: int = Kernel().getWorker().getFrame(TinselFrame).currentTitle
        if titleId:
            return Title.getTitleById(titleId)
        playerInfo = self.getEntityInfos()
        if playerInfo and playerInfo.humanoidInfo:
            for option in playerInfo.humanoidInfo.options:
                if isinstance(option, HumanOptionTitle):
                    titleId = option.titleId
            return Title.getTitleById(titleId)
        return None

    def getOrnament(self) -> Ornament:
        ornament: Ornament = None
        ornamentId: int = Kernel().getWorker().getFrame(TinselFrame).currentOrnament
        if ornamentId:
            return Ornament.getOrnamentById(ornamentId)
        return None

    def getKnownTitles(self) -> list[int]:
        return Kernel().getWorker().getFrame(TinselFrame).knownTitles

    def getKnownOrnaments(self) -> list[int]:
        return Kernel().getWorker().getFrame(TinselFrame).knownOrnaments

    def titlesOrnamentsAskedBefore(self) -> bool:
        return Kernel().getWorker().getFrame(TinselFrame).titlesOrnamentsAskedBefore

    def getEntityInfos(self) -> GameRolePlayCharacterInformations:
        import com.ankamagames.dofus.logic.game.fight.frames.FightEntitiesFrame as fightEntitiesFrame
        entitiesFrame: AbstractEntitiesFrame = None
        if self.isInFight():
            entitiesFrame = Kernel().getFrame(fightEntitiesFrame.FightEntitiesFrame)
            entitiesFrame = Kernel().getFrame(RoleplayEntitiesFrame)
        if not entitiesFrame:
            return None
        return entitiesFrame.getEntityInfos(PlayedCharacterManager().id)

    # def getEntityTooltipInfos(self) -> CharacterTooltipInformation:
    #     playerInfo: GameRolePlayCharacterInformations = self.getEntityInfos()
    #     if not playerInfo:
    #         return None
    #     return CharacterTooltipInformation(playerInfo, 0)

    def getKamasMaxLimit(self) -> float:
        playedCharacterFrame: pcuF.PlayedCharacterUpdatesFrame = (
            Kernel().getWorker().getFrame(pcuF.PlayedCharacterUpdatesFrame)
        )
        if playedCharacterFrame:
            return playedCharacterFrame.kamasLimit
        return 0

    def inventoryWeight(self) -> int:
        return PlayedCharacterManager().inventoryWeight

    def shopWeight(self) -> int:
        return PlayedCharacterManager().shopWeight

    def inventoryWeightMax(self) -> int:
        return PlayedCharacterManager().inventoryWeightMax

    def isIncarnation(self) -> bool:
        return PlayedCharacterManager().isIncarnation

    def isMutated(self) -> bool:
        return PlayedCharacterManager().isMutated

    def isInHouse(self) -> bool:
        return PlayedCharacterManager().isInHouse

    def isIndoor(self) -> bool:
        return PlayedCharacterManager().isIndoor

    def isInExchange(self) -> bool:
        return PlayedCharacterManager().isInExchange

    def isInFight(self) -> bool:
        from com.ankamagames.dofus.logic.game.fight.frames.FightContextFrame import (
            FightContextFrame,
        )

        return Kernel().getWorker().getFrame(FightContextFrame) != None

    def isInPreFight(self) -> bool:
        return Kernel().getWorker().contains(
            FightPreparationFrame
        ) or Kernel().getWorker().isBeingAdded(FightPreparationFrame)

    def isSpectator(self) -> bool:
        return PlayedCharacterManager().isSpectator

    def isInParty(self) -> bool:
        return PlayedCharacterManager().isInParty

    def isPartyLeader(self) -> bool:
        return PlayedCharacterManager().isPartyLeader

    def isRidding(self) -> bool:
        return PlayedCharacterManager().isRidding

    def isPetsMounting(self) -> bool:
        return PlayedCharacterManager().isPetsMounting

    def hasCompanion(self) -> bool:
        return PlayedCharacterManager().hasCompanion

    def id(self) -> float:
        return PlayedCharacterManager().id

    def restrictions(self) -> ActorRestrictionsInformations:
        return PlayedCharacterManager().restrictions

    def isMutant(self) -> bool:
        rcf: RoleplayContextFrame = Kernel().getWorker().getFrame(RoleplayContextFrame)
        infos: GameRolePlayActorInformations = rcf.entitiesFrame.getEntityInfos(
            PlayedCharacterManager().id
        )
        return infos is GameRolePlayMutantInformations

    def publicMode(self) -> bool:
        return PlayedCharacterManager().publicMode

    def artworkId(self) -> int:
        return PlayedCharacterManager().artworkId

    def isCreature(self) -> bool:
        return EntitiesLooksManager().isCreature(self.id())

    def getBone(self) -> int:
        i: CharacterBaseInformations = PlayedCharacterManager().infos
        return EntityLookAdapter.fromNetwork(i.entityLook).getBone()

    def getSkin(self) -> int:
        i: CharacterBaseInformations = PlayedCharacterManager().infos
        if (
            EntityLookAdapter.fromNetwork(i.entityLook)
            and EntityLookAdapter.fromNetwork(i.entityLook).getSkins()
            and EntityLookAdapter.fromNetwork(i.entityLook).getSkins().length > 0
        ):
            return EntityLookAdapter.fromNetwork(i.entityLook).getSkins()[0]
        return 0

    def getColors(self) -> list:
        i: CharacterBaseInformations = PlayedCharacterManager().infos
        return EntityLookAdapter.fromNetwork(i.entityLook).getColors()

    # def getSubentityColors(self) -> list:
    #        i:CharacterBaseInformations = PlayedCharacterManager().infos
    #    subTel:TiphonEntityLook = EntityLookAdapter.fromNetwork(i.entityLook).getSubEntity(SubEntityBindingPointCategoryEnum.HOOK_POINT_CATEGORY_MOUNT_DRIVER,0)
    #    if not subTel and PlayedCharacterManager().realEntityLook:
    #       subTel = EntityLookAdapter.fromNetwork(PlayedCharacterManager().realEntityLook).getSubEntity(SubEntityBindingPointCategoryEnum.HOOK_POINT_CATEGORY_MOUNT_DRIVER,0)
    #    return !not subTel ? subTel.getColors() : None

    def getAlignmentSide(self) -> int:
        if PlayedCharacterManager().characteristics:
            return PlayedCharacterManager().characteristics.alignmentInfos.alignmentSide
        return AlignmentSideEnum.ALIGNMENT_NEUTRAL

    def getAlignmentValue(self) -> int:
        return PlayedCharacterManager().characteristics.alignmentInfos.alignmentValue

    def getAlignmentAggressableStatus(self) -> int:
        return PlayedCharacterManager().characteristics.alignmentInfos.aggressable

    def getAlignmentGrade(self) -> int:
        return PlayedCharacterManager().characteristics.alignmentInfos.alignmentGrade

    def getMaxSummonedCreature(self) -> int:
        return CurrentPlayedFighterManager().getMaxSummonedCreature()

    def getCurrentSummonedCreature(self) -> int:
        return CurrentPlayedFighterManager().getCurrentSummonedCreature()

    def canSummon(self) -> bool:
        return CurrentPlayedFighterManager().canSummon()

    def getSpell(self, spellId: int) -> "SpellWrapper":
        return CurrentPlayedFighterManager().getSpellById(spellId)

    def canCastThisSpell(self, spellId: int, lvl: int) -> bool:
        return CurrentPlayedFighterManager().canCastThisSpell(spellId, lvl)

    def canCastThisSpellWithResult(
        self, spellId: int, lvl: int, target: float = 0
    ) -> str:
        resultA: list = ["."]
        CurrentPlayedFighterManager().canCastThisSpell(spellId, lvl, target, resultA)
        return resultA[0]

    def canCastThisSpellOnTarget(
        self, spellId: int, lvl: int, pTargetId: float
    ) -> bool:
        return CurrentPlayedFighterManager().canCastThisSpell(spellId, lvl, pTargetId)

    def isInHisHouse(self) -> bool:
        return PlayedCharacterManager().isInHisHouse

    def getPlayerHouses(self) -> list[HouseWrapper]:
        return Kernel().getWorker().getFrame(HouseFrame).accountHouses

    def currentMap(self) -> WorldPointWrapper:
        return PlayedCharacterManager().currentMap

    def previousMap(self) -> WorldPointWrapper:
        return PlayedCharacterManager().previousMap

    def previousWorldMapId(self) -> int:
        return PlayedCharacterManager().previousWorldMapId

    def previousSubArea(self) -> SubArea:
        return PlayedCharacterManager().previousSubArea

    def currentSubArea(self) -> SubArea:
        return PlayedCharacterManager().currentSubArea

    def isInTutorialArea(self) -> bool:
        subarea: SubArea = PlayedCharacterManager().currentSubArea
        return subarea and subarea.id == DataEnum.SUBAREA_TUTORIAL

    def state(self) -> int:
        return PlayedCharacterManager().state

    def isAlive(self) -> bool:
        return (
            PlayedCharacterManager().state
            == PlayerLifeStatusEnum.STATUS_ALIVE_AND_KICKING
        )

    def getFollowingPlayerIds(self) -> list[float]:
        return PlayedCharacterManager().followingPlayerIds

    def getPlayerSet(self, objectGID: int) -> PlayerSetInfo:
        return pcuF.PlayedCharacterUpdatesFrame(
            Kernel().getWorker().getFrame(pcuF.PlayedCharacterUpdatesFrame)
        ).getPlayerSet(objectGID)

    def getWeapon(self) -> WeaponWrapper:
        build: BuildWrapper = None
        iw: ItemWrapper = None
        if InventoryManager().currentBuildId != -1:
            for build in InventoryManager().builds:
                if build.id == InventoryManager().currentBuildId:
                    break
            for iw in build.equipment:
                if isinstance(iw, WeaponWrapper):
                    break
            if iw:
                return iw
            return None
        return PlayedCharacterManager().currentWeapon

    def getExperienceBonusPercent(self) -> int:
        return PlayedCharacterManager().experiencePercent

    def getAchievementPoints(self) -> int:
        return PlayedCharacterManager().achievementPoints

    def getWaitingGifts(self) -> list:
        return PlayedCharacterManager().waitingGifts

    def getSoloIdols(self) -> list[int]:
        return PlayedCharacterManager().soloIdols

    def getPartyIdols(self) -> list[int]:
        return PlayedCharacterManager().partyIdols

    def setPartyIdols(self, pIdols: list[int]) -> None:
        PlayedCharacterManager().partyIdols = pIdols

    def getIdolsPresets(self) -> list["IdolsPresetWrapper"]:
        return PlayedCharacterManager().idolsPresets

    def isInHisHavenbag(self) -> bool:
        return PlayedCharacterManager().isInHisHavenbag

    def isInHavenbag(self) -> bool:
        return PlayedCharacterManager().isInHavenbag

    def havenbagSharePermissions(self) -> int:
        hbFrame: HavenbagFrame = Kernel().getWorker().getFrame(HavenbagFrame)
        return hbFrame.sharePermissions

    def isInBreach(self) -> bool:
        return PlayedCharacterManager().isInBreach

    def isInBreachSubArea(self) -> bool:
        return (
            PlayedCharacterManager().currentSubArea.id == 904
            or PlayedCharacterManager().currentSubArea.id == 938
        )

    def isInAnomaly(self) -> bool:
        return PlayedCharacterManager().isInAnomaly

    def hasDebt(self) -> bool:
        return DebtManager().hasDebt()

    def getKamaDebt(self) -> int:
        return DebtManager().getTotalKamaDebt()

    def getApplicationInfo(self) -> GuildApplicationInformation:
        return PlayedCharacterManager().applicationInfo

    def getGuildApplicationInfo(self) -> GuildInformations:
        return PlayedCharacterManager().guildApplicationInfo

    def getPlayerApplicationInformation(self) -> object:
        class o:
            pass

        o.guildInfo = PlayedCharacterManager().guildApplicationInfo
        o.applicationInfo = PlayedCharacterManager().applicationInfo
        return o

    def isInKoli(self) -> bool:
        return PlayedCharacterManager().isInKoli

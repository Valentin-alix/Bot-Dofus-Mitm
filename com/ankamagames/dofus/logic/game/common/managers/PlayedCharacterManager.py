from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
    from com.ankamagames.dofus.internalDatacenter.items.WeaponWrapper import (
        WeaponWrapper,
    )
    from com.ankamagames.dofus.internalDatacenter.mount.MountData import MountData
    from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import (
        CharacterBaseInformations,
    )
    from com.ankamagames.dofus.internalDatacenter.stats.EntityStats import EntityStats
    from com.ankamagames.dofus.datacenter.world.SubArea import SubArea
    from com.ankamagames.dofus.datacenter.world.WorldMap import WorldMap
    from com.ankamagames.dofus.internalDatacenter.jobs.KnownJobWrapper import (
        KnownJobWrapper,
    )
    from com.ankamagames.dofus.internalDatacenter.world.WorldPointWrapper import (
        WorldPointWrapper,
    )
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import (
        CharacterCharacteristicsInformations,
    )
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import (
        ActorRestrictionsInformations,
    )
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import (
    CharacterInventoryPositionEnum,
)
from com.ankamagames.dofus.network.enums.PlayerLifeStatusEnum import (
    PlayerLifeStatusEnum,
)
from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import (
    HavenBagRoomPreviewInformation,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.network.ProtocolConstantsEnum import ProtocolConstantsEnum
from com.ankamagames.jerakine.interfaces.IDestroyable import IDestroyable
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.types.Callback import Callback
from com.ankamagames.jerakine.types.positions.MapPoint import Point
from damageCalculation.tools import StatIds

logger = Logger(__name__)


class PlayedCharacterManager(IDestroyable, metaclass=Singleton):
    def __init__(self):
        self._followingPlayerIds = list[float]()
        self._soloIdols = list[int]()
        self._partyIdols = list[int]()
        self._infosAvailableCallbacks = list[Callback]()
        self.playerForgettableSpelldict = dict()
        self.lastCoord = Point(0, 0)
        self.waitingGifts = list()
        self._infos = None
        self._currentSubArea: "SubArea" = None
        self._currentMap: "WorldPointWrapper" = None
        self.previousMap: "WorldPointWrapper" = None
        self.previousSubArea: "SubArea" = None
        self.previousWorldMapId: int = 0
        self.jobs = list()
        self.isInExchange = False
        self.isInHisHouse = False
        self.isInHouse = False
        self.isIndoor = False
        self.isInHisHavenbag = False
        self.isInHavenbag = False
        self.currentHavenbagRooms = list[HavenBagRoomPreviewInformation]()
        self.isInBreach = False
        self.isInAnomaly = False
        self.restrictions: "ActorRestrictionsInformations" = None
        self.realEntityLook: "EntityLook" = None
        self.characteristics: "CharacterCharacteristicsInformations" = None
        self.spellsInventory = list()
        self.playerSpellList = list()
        self.playerShortcutList = list()
        self.inventory = list["ItemWrapper"]()
        self.currentWeapon = None
        self.inventoryWeight = 0
        self.shopWeight = 0
        self.inventoryWeightMax = 0
        self.state = 0
        self.publicMode = False
        self.isRidding = False
        self.isPetsMounting = False
        self.petsMount = None
        self.hasCompanion = False
        self.mount = None
        self.isFighting = False
        self.fightId = -1
        self.teamId = 0
        self.isSpectator = False
        self.experiencePercent = 0
        self.achievementPoints = 0
        self.achievementPercent = 0
        self.applicationInfo = None
        self.guildApplicationInfo = None
        self.speedAjust: int = 0
        self.isInParty: bool = False
        self.playerMaxForgettableSpellsfloat: int = -1
        self._knownZaapMapIds: list[float] = list()
        self._isPartyLeader: bool = False
        super().__init__()

    @property
    def id(self) -> float:
        if self.infos:
            return self.infos.id
        return 0

    @id.setter
    def id(self, id: float) -> None:
        if self.infos:
            self.infos.id = id

    @property
    def infos(self) -> "CharacterBaseInformations":
        return self._infos

    @infos.setter
    def infos(self, pInfos: "CharacterBaseInformations") -> None:
        callback: Callback = None
        self._infos = pInfos
        for callback in self._infosAvailableCallbacks:
            callback.exec()

    @property
    def cantMinimize(self) -> bool:
        return self.restrictions.cantMinimize

    @property
    def forceSlowWalk(self) -> bool:
        return self.restrictions.forceSlowWalk

    @property
    def cantUseTaxCollector(self) -> bool:
        return self.restrictions.cantUseTaxCollector

    @property
    def cantTrade(self) -> bool:
        return self.restrictions.cantTrade

    @property
    def cantRun(self) -> bool:
        return self.restrictions.cantRun

    @property
    def cantMove(self) -> bool:
        return self.restrictions.cantMove

    @property
    def cantBeChallenged(self) -> bool:
        return self.restrictions.cantBeChallenged

    @property
    def cantBeAttackedByMutant(self) -> bool:
        return self.restrictions.cantBeAttackedByMutant

    @property
    def cantBeAggressed(self) -> bool:
        return self.restrictions.cantBeAggressed

    @property
    def cantAttack(self) -> bool:
        return self.restrictions.cantAttack

    @property
    def cantAgress(self) -> bool:
        return self.restrictions.cantAggress

    @property
    def cantChallenge(self) -> bool:
        return self.restrictions.cantChallenge

    @property
    def cantExchange(self) -> bool:
        return self.restrictions.cantExchange

    @property
    def cantChat(self) -> bool:
        return self.restrictions.cantChat

    @property
    def cantBeMerchant(self) -> bool:
        return self.restrictions.cantBeMerchant

    @property
    def cantUseobject(self) -> bool:
        return self.restrictions.cantUseobject

    @property
    def cantUseInteractiveobject(self) -> bool:
        return self.restrictions.cantUseInteractive

    @property
    def cantSpeakToNpc(self) -> bool:
        return self.restrictions.cantSpeakToNPC

    @property
    def cantChangeZone(self) -> bool:
        return self.restrictions.cantChangeZone

    @property
    def cantAttackMonster(self) -> bool:
        return self.restrictions.cantAttackMonster

    @property
    def isInKoli(self) -> bool:
        from com.ankamagames.dofus.logic.game.fight.frames.FightContextFrame import (
            FightContextFrame,
        )
        from com.ankamagames.dofus.kernel.Kernel import Kernel

        fightContextFrame: FightContextFrame = (
            Kernel().getWorker().getFrame(FightContextFrame)
        )
        return fightContextFrame and fightContextFrame.isKolossium

    @property
    def limitedLevel(self) -> int:
        if self.infos:
            if self.infos.level > ProtocolConstantsEnum.MAX_LEVEL:
                return ProtocolConstantsEnum.MAX_LEVEL
            return self.infos.level
        return 0

    @property
    def currentWorldMap(self) -> "WorldMap":
        if self.currentSubArea:
            return self.currentSubArea.worldmap
        return None

    @property
    def currentMap(self) -> "WorldPointWrapper":
        return self._currentMap

    @property
    def currentSubArea(self) -> "SubArea":
        return self._currentSubArea

    @property
    def currentWorldMapId(self) -> int:
        if self.currentSubArea and self.currentSubArea.worldmap:
            return self.currentSubArea.worldmap.id
        return -1

    @property
    def isMutated(self) -> bool:
        l: int = 0
        i: int = 0
        rpBuffs = InventoryManager().inventory.getView("roleplayBuff").content
        if rpBuffs:
            l = len(rpBuffs)
            for i in range(l):
                if (
                    rpBuffs[i]
                    and rpBuffs[i].typeId == DataEnum.ITEM_TYPE_MUTATIONS
                    and rpBuffs[i].position
                    == CharacterInventoryPositionEnum.INVENTORY_POSITION_MUTATION
                ):
                    return True
        return False

    @property
    def isPartyLeader(self) -> bool:
        return self._isPartyLeader

    @isPartyLeader.setter
    def isPartyLeader(self, b: bool) -> None:
        if not self.isInParty:
            self._isPartyLeader = False
        else:
            self._isPartyLeader = b

    @property
    def isGhost(self) -> bool:
        return self.state == PlayerLifeStatusEnum.STATUS_PHANTOM

    @property
    def artworkId(self) -> int:
        return (
            self.infos.entityLook.bonesId == int(self.infos.entityLook.skins[0])
            if 1
            else int(self.infos.entityLook.bonesId)
        )

    @property
    def followingPlayerIds(self) -> list[float]:
        return self._followingPlayerIds

    @currentMap.setter
    def currentMap(self, map: "WorldPointWrapper") -> None:
        if self._currentMap:
            if map.mapId != self._currentMap.mapId:
                self.previousMap = self._currentMap
                self._currentMap = map
            elif not self.isInHavenbag:
                self._currentMap.setOutdoorCoords(map.outdoorX, map.outdoorY)
            else:
                self._currentMap.setOutdoorCoords(
                    self.previousMap.outdoorX, self.previousMap.outdoorY
                )
        else:
            self._currentMap = map

    @currentSubArea.setter
    def currentSubArea(self, area: "SubArea") -> None:
        if not self._currentSubArea or area != self._currentSubArea:
            if self.currentSubArea and self.currentSubArea.worldmap:
                self.previousWorldMapId = self._currentSubArea.worldmap.id
                self.previousSubArea = self.currentSubArea
            self._currentSubArea = area

    @followingPlayerIds.setter
    def followingPlayerIds(self, pPlayerIds: list[float]) -> None:
        self._followingPlayerIds = pPlayerIds

    @property
    def soloIdols(self) -> list[int]:
        return self._soloIdols

    @soloIdols.setter
    def soloIdols(self, pIdols: list[int]) -> None:
        self._soloIdols = pIdols

    @property
    def partyIdols(self) -> list[int]:
        return self._partyIdols

    @partyIdols.setter
    def partyIdols(self, pIdols: list[int]) -> None:
        self._partyIdols = pIdols

    @property
    def canBeAggressedByMonsters(self) -> bool:
        stats: "EntityStats" = StatsManager().getStats(self.id)
        if stats == None:
            return True
        if stats.getStatTotalValue(StatIds.ENERGY_POINTS) == 0:
            return False
        return not self.restrictions.cantAttackMonster

    def levelDiff(self, targetLevel: int) -> int:
        diff: int = 0
        playerLevel: int = self.limitedLevel
        if targetLevel > ProtocolConstantsEnum.MAX_LEVEL:
            targetLevel = ProtocolConstantsEnum.MAX_LEVEL
        type: int = 1
        if targetLevel < playerLevel:
            type = -1
        if abs(targetLevel - playerLevel) > 20:
            diff = 1 * type
        elif targetLevel > playerLevel:
            if targetLevel / playerLevel < 1.2:
                diff = 0
            else:
                diff = 1 * type
        elif playerLevel / targetLevel < 1.2:
            diff = 0
        else:
            diff = 1 * type
        return diff

    def addInfosAvailableCallback(self, pCallback: Callback) -> None:
        self._infosAvailableCallbacks.append(pCallback)

    def jobsLevel(self) -> int:
        job: "KnownJobWrapper" = None
        jobsLevel: int = 0
        for job in self.jobs:
            jobsLevel += job.jobLevel
        return jobsLevel

    def jobsfloat(self, onlyLevelOne: bool = False) -> int:
        job: "KnownJobWrapper" = None
        length: int = 0
        for job in self.jobs:
            if not (job.jobLevel != 1 and onlyLevelOne):
                length += 1
        return length

    def updateKnownZaaps(self, knownZaapMapIds: list[float]) -> None:
        self._knownZaapMapIds = knownZaapMapIds

    def isZaapKnown(self, mapId: float) -> bool:
        if self._knownZaapMapIds == None or len(self._knownZaapMapIds) <= 0:
            return False
        return mapId in self._knownZaapMapIds

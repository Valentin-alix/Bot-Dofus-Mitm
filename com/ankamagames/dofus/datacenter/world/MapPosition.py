from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.DataStoreEnum import DataStoreEnum

logger = Logger(__name__)


class MapPosition(IDataCenter):

    MODULE: str = "MapPositions"

    DST: DataStoreType = DataStoreType(
        MODULE, True, DataStoreEnum.LOCATION_LOCAL, DataStoreEnum.BIND_COMPUTER
    )

    CAPABILITY_ALLOW_CHALLENGE: int = 1

    CAPABILITY_ALLOW_AGGRESSION: int = 2

    CAPABILITY_ALLOW_TELEPORT_TO: int = 4

    CAPABILITY_ALLOW_TELEPORT_FROM: int = 8

    CAPABILITY_ALLOW_EXCHANGES_BETWEEN_PLAYERS: int = 16

    CAPABILITY_ALLOW_HUMAN_VENDOR: int = 32

    CAPABILITY_ALLOW_COLLECTOR: int = 64

    CAPABILITY_ALLOW_SOUL_CAPTURE: int = 128

    CAPABILITY_ALLOW_SOUL_SUMMON: int = 256

    CAPABILITY_ALLOW_TAVERN_REGEN: int = 512

    CAPABILITY_ALLOW_TOMB_MODE: int = 1024

    CAPABILITY_ALLOW_TELEPORT_EVERYWHERE: int = 2048

    CAPABILITY_ALLOW_FIGHT_CHALLENGES: int = 4096

    CAPABILITY_ALLOW_MONSTER_RESPAWN: int = 8192

    CAPABILITY_ALLOW_MONSTER_FIGHT: int = 16384

    CAPABILITY_ALLOW_MOUNT: int = 32768

    CAPABILITY_ALLOW_OBJECT_DISPOSAL: int = 65536

    CAPABILITY_ALLOW_UNDERWATER: int = 131072

    CAPABILITY_ALLOW_PVP_1V1: int = 262144

    CAPABILITY_ALLOW_PVP_3V3: int = 524288

    CAPABILITY_ALLOW_MONSTER_AGRESSION: int = 1048576

    id: float

    posX: int

    posY: int

    outdoor: bool

    capabilities: int

    nameId: int

    showNameOnFingerpost: bool

    playlists: list[list[int]]

    subAreaId: int

    worldMap: int

    hasPriorityOnWorldmap: bool

    allowPrism: bool

    isTransition: bool

    mapHasTemplate: bool

    tacticalModeTemplateId: int

    hasPublicPaddock: bool

    def __init__(self):
        self._name = ""
        self.id = None
        self.posX = None
        self.posY = None
        self._subArea = None
        super().__init__()

    @staticmethod
    def getMapPositionById(id: float) -> "MapPosition":
        return GameData.getObject(MapPosition.MODULE, id)

    @staticmethod
    def getMapPositions() -> list:
        return GameData.getobjects(MapPosition.MODULE)

    @staticmethod
    def getMapIdByCoord(x: int, y: int) -> list[float]:
        from com.ankamagames.dofus.datacenter.world.MapCoordinates import MapCoordinates

        mc: MapCoordinates = MapCoordinates.getMapCoordinatesByCoords(x, y)
        if mc:
            return mc.mapIds
        return None

    idAccessors: IdAccessors = IdAccessors(getMapPositionById, getMapPositions)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def subArea(self) -> "SubArea":
        from com.ankamagames.dofus.datacenter.world.SubArea import SubArea

        if not self._subArea:
            self._subArea = SubArea.getSubAreaById(self.subAreaId)
        return self._subArea

    @property
    def allowChallenge(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_CHALLENGE) != 0

    @property
    def allowAggression(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_AGGRESSION) != 0

    @property
    def allowTeleportTo(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_TELEPORT_TO) != 0

    @property
    def allowTeleportFrom(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_TELEPORT_FROM) != 0

    @property
    def allowExchanges(self) -> bool:
        return (
            self.capabilities & self.CAPABILITY_ALLOW_EXCHANGES_BETWEEN_PLAYERS
        ) != 0

    @property
    def allowHumanVendor(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_HUMAN_VENDOR) != 0

    @property
    def allowTaxCollector(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_COLLECTOR) != 0

    @property
    def allowSoulCapture(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_SOUL_CAPTURE) != 0

    @property
    def allowSoulSummon(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_SOUL_SUMMON) != 0

    @property
    def allowTavernRegen(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_TAVERN_REGEN) != 0

    @property
    def allowTombMode(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_TOMB_MODE) != 0

    @property
    def allowTeleportEverywhere(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_TELEPORT_EVERYWHERE) != 0

    @property
    def allowFightChallenges(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_FIGHT_CHALLENGES) != 0

    @property
    def allowMonsterRespawn(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_MONSTER_RESPAWN) != 0

    @property
    def allowMonsterFight(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_MONSTER_FIGHT) != 0

    @property
    def allowMount(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_MOUNT) != 0

    @property
    def allowobjectDisposal(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_OBJECT_DISPOSAL) != 0

    @property
    def isUnderWater(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_UNDERWATER) != 0

    @property
    def allowPvp1v1(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_PVP_1V1) != 0

    @property
    def allowPvp3v3(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_PVP_3V3) != 0

    @property
    def allowMonsterAggression(self) -> bool:
        return (self.capabilities & self.CAPABILITY_ALLOW_MONSTER_AGRESSION) != 0

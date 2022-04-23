from com.ankamagames.dofus.datacenter.servers.ServerCommunity import ServerCommunity
from com.ankamagames.dofus.datacenter.servers.ServerGameType import ServerGameType
from com.ankamagames.dofus.datacenter.servers.ServerPopulation import ServerPopulation
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter

logger = Logger(__name__)


class Server(IDataCenter):

    MODULE: str = "Servers"

    def __init__(self):
        self.id: int = None

        self.nameId: int = None

        self.commentId: int = None

        self.openingDate: float = None

        self.language: str = None

        self.populationId: int = None

        self.gameTypeId: int = None

        self.communityId: int = None

        self.restrictedToLanguages = list[str]()

        self.monoAccount: bool = None

        self._name: str = None

        self._comment: str = None

        self._gameType: ServerGameType = None

        self._community: ServerCommunity = None

        self._population: ServerPopulation = None

        super().__init__()

    @staticmethod
    def getServerById(id: int) -> "Server":
        return GameData.getObject(Server.MODULE, id)

    @staticmethod
    def getServers(self) -> list:
        return GameData.getObjects(Server.MODULE)

    idAccessors: IdAccessors = IdAccessors(getServerById, getServers)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def comment(self) -> str:
        if not self._comment:
            self._comment = I18n.getText(self.commentId)
        return self._comment

    @property
    def gameType(self) -> ServerGameType:
        if not self._gameType or self._gameType.id != self.gameTypeId:
            self._gameType = ServerGameType.getServerGameTypeById(self.gameTypeId)
        return self._gameType

    @property
    def community(self) -> ServerCommunity:
        if not self._community or self._community.id != self.communityId:
            self._community = ServerCommunity.getServerCommunityById(self.communityId)
        return self._community

    @property
    def population(self) -> ServerPopulation:
        if not self._population:
            self._population = ServerPopulation.getServerPopulationById(
                self.populationId
            )
        return self._population

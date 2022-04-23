from types import FunctionType
from com.ankamagames.dofus.datacenter.servers.Server import Server
import com.ankamagames.dofus.kernel.Kernel as krnl
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
from com.ankamagames.dofus.kernel.net.DisconnectionReasonEnum import (
    DisconnectionReasonEnum,
)
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.connection.actions.ServerSelectionAction import (
    ServerSelectionAction,
)
from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager import (
    AuthentificationManager,
)
from com.ankamagames.dofus.network.enums.ServerStatusEnum import ServerStatusEnum
from com.ankamagames.dofus.network.messages.connection.SelectedServerDataExtendedMessage import (
    SelectedServerDataExtendedMessage,
)
from com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import (
    SelectedServerDataMessage,
)
from com.ankamagames.dofus.network.messages.connection.ServerStatusUpdateMessage import (
    ServerStatusUpdateMessage,
)
from com.ankamagames.dofus.network.messages.connection.ServersListMessage import (
    ServersListMessage,
)
from com.ankamagames.dofus.network.types.connection.GameServerInformations import (
    GameServerInformations,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.messages.WrongSocketClosureReasonMessage import (
    WrongSocketClosureReasonMessage,
)
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.jerakine.network.messages.ExpectedSocketClosureMessage import (
    ExpectedSocketClosureMessage,
)
from com.ankamagames.jerakine.network.messages.Worker import Worker
from com.ankamagames.jerakine.types.enums.Priority import Priority
from pyd2bot.events.BotEventsManager import BotEventsManager

logger = Logger(__name__)


class ServerSelectionFrame(Frame):

    _serversList: list[GameServerInformations]

    _serversUsedList: list[GameServerInformations]

    _serversTypeAvailableSlots: dict

    _selectedServer: SelectedServerDataMessage

    _worker: Worker

    _alreadyConnectedToServerId: int = 0

    _serverSelectionAction: ServerSelectionAction

    _connexionPorts: list

    def __init__(self):
        self._serversTypeAvailableSlots = dict()
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.HIGH

    @property
    def usedServers(self) -> list[GameServerInformations]:
        return self._serversUsedList

    @property
    def servers(self) -> list[GameServerInformations]:
        return self._serversList

    @property
    def availableSlotsByServerType(self) -> list:
        return self._serversTypeAvailableSlots

    def pushed(self) -> bool:
        self._worker = krnl.Kernel().getWorker()
        return True

    def process(self, msg: Message) -> bool:

        if isinstance(msg, ServersListMessage):
            slmsg = msg
            PlayerManager().server = None
            self._serversList = slmsg.servers
            self._serversList.sort(key=lambda x: x.date)
            self.broadcastServersListUpdate()
            BotEventsManager().dispatch(BotEventsManager.SERVER_SELECTION)
            return True

        elif isinstance(msg, ServerStatusUpdateMessage):
            ssumsg = msg
            serverHasBeenUpdated = False
            for knownServer in self._serversList:
                if ssumsg.server.id == knownServer.id:
                    knownServer.charactersCount = ssumsg.server.charactersCount
                    knownServer.completion = ssumsg.server.completion
                    knownServer.isSelectable = ssumsg.server.isSelectable
                    knownServer.status = ssumsg.server.status
                    serverHasBeenUpdated = True
            if not serverHasBeenUpdated:
                self._serversList.append(ssumsg.server)
                self._serversList.sort(key=lambda x: x.date)
            logger.info(
                f"Server {ssumsg.server.id} status changed to {ssumsg.server.status}."
            )
            self.broadcastServersListUpdate()
            return True

        elif isinstance(msg, ServerSelectionAction):
            ssaction = msg

            if (
                self._alreadyConnectedToServerId > 0
                and ssaction.serverId != self._alreadyConnectedToServerId
            ):
                self._serverSelectionAction = ssaction
                self.serverAlreadyInName = Server.getServerById(
                    self._alreadyConnectedToServerId
                ).name
                self.serverSelectedName = Server.getServerById(ssaction.serverId).name
                return True

            for server in self._serversList:
                if server.id == ssaction.serverId:
                    if (
                        ServerStatusEnum(server.status) == ServerStatusEnum.ONLINE
                        or ServerStatusEnum(server.status) == ServerStatusEnum.NOJOIN
                    ):
                        ssmsg = NetworkMessage.from_json(
                            {
                                "__type__": "ServerSelectionMessage",
                                "serverId": ssaction.serverId,
                            }
                        )
                        connh.ConnectionsHandler.getConnection().send(ssmsg)
                    else:
                        errorText = "Status " + ServerStatusEnum(server.status).name
                else:
                    errorText = "Status Unknown"
            return True

        elif isinstance(msg, SelectedServerDataExtendedMessage):
            ssdemsg = msg
            self._serversList = ssdemsg.servers
            self._serversList.sort(key=lambda x: x.date)
            self.broadcastServersListUpdate(True)
            return True

        elif isinstance(msg, ExpectedSocketClosureMessage):
            from com.ankamagames.dofus.logic.game.approach.frames.GameServerApproachFrame import (
                GameServerApproachFrame,
            )

            escmsg = msg
            if escmsg.reason != DisconnectionReasonEnum.SWITCHING_TO_GAME_SERVER:
                self._worker.process(
                    WrongSocketClosureReasonMessage(
                        DisconnectionReasonEnum.SWITCHING_TO_GAME_SERVER, escmsg.reason
                    )
                )
                return True
            self._worker.addFrame(GameServerApproachFrame())
            connh.ConnectionsHandler.connectToGameServer(
                self._selectedServer.address, self._selectedServer.ports[0]
            )
            return True

        elif isinstance(msg, SelectedServerDataMessage):
            ssdmsg = msg
            connh.ConnectionsHandler.connectionGonnaBeClosed(
                DisconnectionReasonEnum.SWITCHING_TO_GAME_SERVER
            )
            self._selectedServer = ssdmsg
            AuthentificationManager().gameServerTicket = (
                AuthentificationManager().decodeWithAES(ssdmsg.ticket).decode()
            )
            PlayerManager().server = Server.getServerById(ssdmsg.serverId)
            PlayerManager().kisServerPort = 0
            self._connexionPorts = []
            for port in ssdmsg.ports:
                self._connexionPorts.append(port)
            logger.debug(
                f"Connection to game server using ports : {self._connexionPorts}"
            )
            BotEventsManager().dispatch(BotEventsManager.SERVER_SELECTED)
            return True

        return False

    def pulled(self) -> bool:
        self._serversList = None
        self._serversUsedList = None
        self._selectedServer = None
        self._worker = None
        return True

    def getSelectableServers(self) -> list:
        server = None
        selectableServers: list = list()
        for server in self._serversList:
            if server.status == ServerStatusEnum.ONLINE and server.isSelectable:
                selectableServers.append(server.id)
        return selectableServers

    def broadcastServersListUpdate(self, silent: bool = False) -> None:
        self._serversTypeAvailableSlots = dict()
        self._serversUsedList = list[GameServerInformations]()
        PlayerManager().serversList = list[int]()
        for server in self._serversList:
            if not self._serversTypeAvailableSlots.get(server.type):
                self._serversTypeAvailableSlots[server.type] = 0
            if server.charactersCount < server.charactersSlots:
                self._serversTypeAvailableSlots[server.type] = 1
            if server.charactersCount > 0:
                self._serversUsedList.append(server)
                PlayerManager().serversList.append(server.id)

    def getUpdateServerStatusFunction(
        self, serverId: int, newStatus: int
    ) -> FunctionType:
        def function(
            element: GameServerInformations,
            index: int,
            arr: list[GameServerInformations],
        ) -> None:
            gsi = element
            if serverId == gsi.id:
                gsi.status = newStatus

        return function

    def onValidServerSelection(self) -> None:
        self._alreadyConnectedToServerId = 0
        self.process(self._serverSelectionAction)
        self._serverSelectionAction = None

    def onCancelServerSelection(self) -> None:
        self._serverSelectionAction = None

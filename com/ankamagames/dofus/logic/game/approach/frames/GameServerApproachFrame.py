from datetime import datetime
from threading import Timer
import time
from com.ankamagames.dofus.internalDatacenter.connection.BasicCharacterWrapper import (
    BasicCharacterWrapper,
)
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper

# from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
import com.ankamagames.dofus.kernel.Kernel as krnl
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
import com.ankamagames.dofus.logic.connection.frames.ServerSelectionFrame as ssfrm
from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager import (
    AuthentificationManager,
)
from com.ankamagames.dofus.logic.common.managers.InterClientManager import (
    InterClientManager,
)
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.game.approach.actions.CharacterSelectionAction import (
    CharacterSelectionAction,
)
from com.ankamagames.dofus.logic.game.common.actions.chat.PopupWarningCloseRequestAction import (
    PopupWarningCloseRequestAction,
)
from com.ankamagames.dofus.logic.game.common.frames.ContextChangeFrame import (
    ContextChangeFrame,
)
from com.ankamagames.dofus.logic.game.common.frames.SynchronisationFrame import (
    SynchronisationFrame,
)
from com.ankamagames.dofus.logic.game.common.frames.WorldFrame import WorldFrame
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.common.managers.TimerManager import TimeManager
from com.ankamagames.dofus.network.messages.game.approach.AccountCapabilitiesMessage import (
    AccountCapabilitiesMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AlreadyConnectedMessage import (
    AlreadyConnectedMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AuthenticationTicketAcceptedMessage import (
    AuthenticationTicketAcceptedMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AuthenticationTicketMessage import (
    AuthenticationTicketMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AuthenticationTicketRefusedMessage import (
    AuthenticationTicketRefusedMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.HelloGameMessage import (
    HelloGameMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicTimeMessage import (
    BasicTimeMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedForceMessage import (
    CharacterSelectedForceMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedForceReadyMessage import (
    CharacterSelectedForceReadyMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedSuccessMessage import (
    CharacterSelectedSuccessMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import (
    CharacterSelectionMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListErrorMessage import (
    CharactersListErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListMessage import (
    CharactersListMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListRequestMessage import (
    CharactersListRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextCreateRequestMessage import (
    GameContextCreateRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.CharacterLoadingCompleteMessage import (
    CharacterLoadingCompleteMessage,
)
from com.ankamagames.dofus.network.messages.game.moderation.PopupWarningCloseRequestMessage import (
    PopupWarningCloseRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.moderation.PopupWarningClosedMessage import (
    PopupWarningClosedMessage,
)
from com.ankamagames.dofus.network.messages.game.startup.StartupActionsListMessage import (
    StartupActionsListMessage,
)
from com.ankamagames.dofus.network.messages.security.ClientKeyMessage import (
    ClientKeyMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.ConnectionResumedMessage import (
    ConnectionResumedMessage,
)
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.jerakine.network.messages.ServerConnectionFailedMessage import (
    ServerConnectionFailedMessage,
)
from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.Priority import Priority
from pyd2bot.events.BotEventsManager import BotEventsManager

logger = Logger(__name__)


class GameServerApproachFrame(Frame):

    LOADING_TIMEOUT: int = 60

    def __init__(self):
        self._charactersList = list[BasicCharacterWrapper]()
        self._giftList = []
        self._charaListMinusDeadPeople = []
        self._cssmsg = None
        self.authenticationTicketAccepted = False
        self._charactersList = list[BasicCharacterWrapper]()
        self._waitingMessages = list[NetworkMessage]()
        self._requestedCharacterId = None
        self._loadingStart = False
        self._reconnectMsgSend = False

        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.NORMAL

    @property
    def giftList(self) -> list:
        return self._giftList

    @property
    def charaListMinusDeadPeople(self) -> list:
        return self._charaListMinusDeadPeople

    @property
    def requestedCharaId(self) -> float:
        return self._requestedCharacterId

    @requestedCharaId.setter
    def requestedCharaId(self, id: float) -> None:
        self._requestedCharacterId = id

    def isCharacterWaitingForChange(self, id: float) -> bool:
        if self._charactersToRemodelList.get(id):
            return True
        return False

    def process(self, msg: Message) -> bool:

        if isinstance(msg, HelloGameMessage):
            connh.ConnectionsHandler.confirmGameServerConnection()
            self.authenticationTicketAccepted = False
            atmsg = AuthenticationTicketMessage.from_json(
                {
                    "__type__": "AuthenticationTicketMessage",
                    "lang": "fr",
                    "ticket": AuthentificationManager().gameServerTicket,
                }
            )
            connh.ConnectionsHandler.getConnection().send(atmsg)
            return True

        elif isinstance(msg, AuthenticationTicketAcceptedMessage):
            Timer(0.5, self.requestCharactersList).start()
            self.authenticationTicketAccepted = True
            return True

        elif isinstance(msg, AuthenticationTicketRefusedMessage):
            self.authenticationTicketAccepted = False
            return True

        elif isinstance(msg, CharactersListMessage):
            clmsg = msg
            self._charactersList = list[BasicCharacterWrapper]()
            for chi in clmsg.characters:
                self._charactersList.append(chi)
            PlayerManager().charactersList = self._charactersList
            BotEventsManager().dispatch(BotEventsManager.CHARACTER_SELECTION)
            return True

        elif isinstance(msg, ServerConnectionFailedMessage):
            scfMsg = ServerConnectionFailedMessage(msg)
            self.authenticationTicketAccepted = False
            if (
                scfMsg.failedConnection
                == connh.ConnectionsHandler.getConnection().getSubConnection(scfMsg)
            ):
                PlayerManager().destroy()
            return True

        elif isinstance(msg, AlreadyConnectedMessage):
            PlayerManager().wasAlreadyConnected = True
            return True

        elif isinstance(msg, CharactersListErrorMessage):
            return False

        elif isinstance(msg, AccountCapabilitiesMessage):
            accmsg = msg
            PlayerManager().adminStatus = accmsg.status
            PlayerManager().canCreateNewCharacter = accmsg.canCreateNewCharacter
            return True

        elif isinstance(msg, CharacterSelectedSuccessMessage):
            import com.ankamagames.dofus.logic.game.common.frames.PlayedCharacterUpdatesFrame as pcuF

            cssmsg = msg
            self._loadingStart = time.perf_counter()
            if krnl.Kernel().getWorker().getFrame(ssfrm.ServerSelectionFrame):
                krnl.Kernel().getWorker().removeFrame(
                    krnl.Kernel().getWorker().getFrame(ssfrm.ServerSelectionFrame)
                )
            PlayedCharacterManager().infos = cssmsg.infos
            DataStoreType.CHARACTER_ID = str(cssmsg.infos.id)
            krnl.Kernel().getWorker().addFrame(WorldFrame())
            krnl.Kernel().getWorker().addFrame(SynchronisationFrame())
            krnl.Kernel().getWorker().addFrame(pcuF.PlayedCharacterUpdatesFrame())
            # krnl.Kernel().getWorker().addFrame(SpellInventoryManagementFrame())
            # krnl.Kernel().getWorker().addFrame(InventoryManagementFrame())
            krnl.Kernel().getWorker().addFrame(ContextChangeFrame())
            # krnl.Kernel().getWorker().addFrame(ProgressionFrame())
            # krnl.Kernel().getWorker().addFrame(ChatFrame())
            # krnl.Kernel().getWorker().addFrame(JobsFrame())
            # krnl.Kernel().getWorker().addFrame(QuestFrame())
            # krnl.Kernel().getWorker().addFrame(PartyManagementFrame())
            # krnl.Kernel().getWorker().addFrame(AveragePricesFrame())
            if krnl.Kernel().beingInReconection and not self._reconnectMsgSend:
                self._reconnectMsgSend = True
                connh.ConnectionsHandler.getConnection().send(
                    CharacterSelectedForceReadyMessage()
                )
            if InterClientManager.flashKey and (
                not PlayerManager()
                or PlayerManager().server.id != 129
                and PlayerManager().server.id != 130
            ):
                flashKeyMsg = ClientKeyMessage.from_json(
                    {
                        "__type__": "ClientKeyMessage",
                        "key": InterClientManager().flashKey,
                    }
                )
                connh.ConnectionsHandler.getConnection().send(flashKeyMsg)
            if self._cssmsg is not None:
                PlayedCharacterManager().infos = self._cssmsg.infos
                DataStoreType.CHARACTER_ID = str(self._cssmsg.infos.id)
            krnl.Kernel().getWorker().removeFrame(self)
            gccrmsg = GameContextCreateRequestMessage()
            connh.ConnectionsHandler.getConnection().send(gccrmsg)
            now = time.perf_counter()
            delta = now - self._loadingStart
            if delta > self.LOADING_TIMEOUT:
                logger.warn(f"Client took too long to load ({delta}s).")
            return True

        elif isinstance(msg, ConnectionResumedMessage):
            return True

        elif isinstance(msg, CharacterSelectedForceMessage):
            logger.error("Impossible to select character, server is full.")
            self._requestedCharacterId = 0
            return True

        elif isinstance(msg, BasicTimeMessage):
            btmsg = msg
            TimeManager().serverTimeLag = (
                btmsg.timestamp
                + btmsg.timezoneOffset * 60 * 1000
                - datetime.now().timestamp()
            )
            TimeManager().serverUtcTimeLag = (
                btmsg.timestamp - datetime.now().timestamp()
            )
            TimeManager().timezoneOffset = btmsg.timezoneOffset * 60 * 1000
            TimeManager().dofusTimeYearLag = -1370
            return True

        elif isinstance(msg, StartupActionsListMessage):
            salm = msg
            self._giftList = []
            for gift in salm.actions:
                _items = []
                for item in gift.items:
                    iw = ItemWrapper.create(
                        0, 0, item.objectGID, item.quantity, item.effects, False
                    )
                    _items.append(iw)
                    oj = {
                        "uid": gift.uid,
                        "title": gift.title,
                        "text": gift.text,
                        "items": _items,
                    }
                self._giftList.append(oj)
            if len(self._giftList):
                self._charaListMinusDeadPeople = []
                for perso in self._charactersList:
                    if not perso.deathState or perso.deathState == 0:
                        self._charaListMinusDeadPeople.append(perso)
            else:
                krnl.Kernel().getWorker().removeFrame(self)
                logger.warn("Empty Gift List Received")
            return True

        elif isinstance(msg, PopupWarningClosedMessage):
            return True

        elif isinstance(msg, PopupWarningCloseRequestAction):
            pwcrmsg = PopupWarningCloseRequestMessage()
            connh.ConnectionsHandler.getConnection().send(pwcrmsg)
            return True

        elif isinstance(msg, CharacterSelectionAction):
            characterId = msg.characterId
            self._requestedCharacterId = characterId
            self._requestedToRemodelCharacterId = 0
            csmsg = CharacterSelectionMessage()
            csmsg.init(id_=characterId)
            connh.ConnectionsHandler.getConnection().send(csmsg)
            return True

        return False

    def pulled(self) -> bool:
        return True

    def pushed(self) -> bool:
        return True

    def requestCharactersList(self) -> None:
        clrmsg: CharactersListRequestMessage = CharactersListRequestMessage()
        if connh.ConnectionsHandler.getConnection():
            connh.ConnectionsHandler.getConnection().send(clrmsg)

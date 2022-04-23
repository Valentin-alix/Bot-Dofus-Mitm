from com.ankamagames.dofus.network.messages.connection.CredentialsAcknowledgementMessage import (
    CredentialsAcknowledgementMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicAckMessage import (
    BasicAckMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicNoOperationMessage import (
    BasicNoOperationMessage,
)
from com.ankamagames.dofus.network.messages.game.character.status.PlayerStatusUpdateMessage import (
    PlayerStatusUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextDestroyMessage import (
    GameContextDestroyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameEntitiesDispositionMessage import (
    GameEntitiesDispositionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSynchronizeMessage import (
    GameFightSynchronizeMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnReadyRequestMessage import (
    GameFightTurnReadyRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.SlaveSwitchContextMessage import (
    SlaveSwitchContextMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterMessage import (
    GameFightShowFighterMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import (
    MapComplementaryInformationsDataMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.OnConnectionEventMessage import (
    OnConnectionEventMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectJobAddedMessage import (
    ObjectJobAddedMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.messages.ConnectionResumedMessage import (
    ConnectionResumedMessage,
)
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.network.messages.ServerConnectionFailedMessage import (
    ServerConnectionFailedMessage,
)
from com.ankamagames.jerakine.types.enums.Priority import Priority

logger = Logger(__name__)


class CleanupCrewFrame(Frame):
    def __init__(self):
        super().__init__()

    @property
    def priority(self) -> int:
        return Priority.LOWEST

    def pushed(self) -> bool:
        return True

    def process(self, msg: Message) -> bool:
        msgClassList = [
            ServerConnectionFailedMessage,
            BasicAckMessage,
            BasicNoOperationMessage,
            CredentialsAcknowledgementMessage,
            OnConnectionEventMessage,
            ObjectJobAddedMessage,
            ConnectionResumedMessage,
            GameEntitiesDispositionMessage,
            GameFightShowFighterMessage,
            GameContextDestroyMessage,
            PlayerStatusUpdateMessage,
            MapComplementaryInformationsDataMessage,
            GameFightTurnReadyRequestMessage,
            GameFightSynchronizeMessage,
            SlaveSwitchContextMessage,
        ]
        if msg.__class__ in msgClassList:
            return True

        else:
            logger.info(
                f"[Warning] {msg.__class__.__name__} wasn't stopped by a frame."
            )
            return True

    def pulled(self) -> bool:
        return True

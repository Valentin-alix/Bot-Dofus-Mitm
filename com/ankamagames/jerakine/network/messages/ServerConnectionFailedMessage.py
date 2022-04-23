from com.ankamagames.jerakine.messages.Message import Message
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.jerakine.network.ServerConnection import ServerConnection


class ServerConnectionFailedMessage(Message):

    _failedConnection: "ServerConnection"

    _errorMessage: str

    def __init__(self, failedConnection: "ServerConnection", errorMessage: str):
        super().__init__()
        self._errorMessage = errorMessage
        self._failedConnection = failedConnection

    @property
    def failedConnection(self) -> "ServerConnection":
        return self._failedConnection

    @property
    def errorMessage(self) -> str:
        return self._errorMessage

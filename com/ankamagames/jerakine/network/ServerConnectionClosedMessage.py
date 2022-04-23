from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.network.ServerConnection import ServerConnection


class ServerConnectionClosedMessage(Message):

    _closedConnection: ServerConnection

    def __init__(self, closedConnection: ServerConnection):
        super().__init__()
        self._closedConnection = closedConnection

    @property
    def closedConnection(self) -> ServerConnection:
        return self._closedConnection

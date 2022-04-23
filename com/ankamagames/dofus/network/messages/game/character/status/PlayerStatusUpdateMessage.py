from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    


class PlayerStatusUpdateMessage(NetworkMessage):
    accountId:int
    playerId:int
    status:'PlayerStatus'
    

    def init(self, accountId_:int, playerId_:int, status_:'PlayerStatus'):
        self.accountId = accountId_
        self.playerId = playerId_
        self.status = status_
        
        super().__init__()
    
    
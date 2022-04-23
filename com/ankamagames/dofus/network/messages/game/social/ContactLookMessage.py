from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class ContactLookMessage(NetworkMessage):
    requestId:int
    playerName:str
    playerId:int
    look:'EntityLook'
    

    def init(self, requestId_:int, playerName_:str, playerId_:int, look_:'EntityLook'):
        self.requestId = requestId_
        self.playerName = playerName_
        self.playerId = playerId_
        self.look = look_
        
        super().__init__()
    
    
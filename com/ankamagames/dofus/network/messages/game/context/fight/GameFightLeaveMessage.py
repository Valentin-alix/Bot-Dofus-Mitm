from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightLeaveMessage(NetworkMessage):
    charId:int
    

    def init(self, charId_:int):
        self.charId = charId_
        
        super().__init__()
    
    
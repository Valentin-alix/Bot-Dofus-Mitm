from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceKickRequestMessage(NetworkMessage):
    kickedId:int
    

    def init(self, kickedId_:int):
        self.kickedId = kickedId_
        
        super().__init__()
    
    
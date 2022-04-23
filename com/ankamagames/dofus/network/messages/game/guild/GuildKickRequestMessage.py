from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildKickRequestMessage(NetworkMessage):
    kickedId:int
    

    def init(self, kickedId_:int):
        self.kickedId = kickedId_
        
        super().__init__()
    
    
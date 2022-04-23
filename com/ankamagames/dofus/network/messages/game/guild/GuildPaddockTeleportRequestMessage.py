from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildPaddockTeleportRequestMessage(NetworkMessage):
    paddockId:int
    

    def init(self, paddockId_:int):
        self.paddockId = paddockId_
        
        super().__init__()
    
    
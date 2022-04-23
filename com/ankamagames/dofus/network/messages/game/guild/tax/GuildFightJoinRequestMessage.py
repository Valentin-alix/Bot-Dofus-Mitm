from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFightJoinRequestMessage(NetworkMessage):
    taxCollectorId:int
    

    def init(self, taxCollectorId_:int):
        self.taxCollectorId = taxCollectorId_
        
        super().__init__()
    
    
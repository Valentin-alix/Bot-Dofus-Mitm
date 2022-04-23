from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildGetInformationsMessage(NetworkMessage):
    infoType:int
    

    def init(self, infoType_:int):
        self.infoType = infoType_
        
        super().__init__()
    
    
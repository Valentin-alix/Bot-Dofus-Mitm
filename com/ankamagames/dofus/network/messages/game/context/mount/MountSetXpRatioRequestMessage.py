from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountSetXpRatioRequestMessage(NetworkMessage):
    xpRatio:int
    

    def init(self, xpRatio_:int):
        self.xpRatio = xpRatio_
        
        super().__init__()
    
    
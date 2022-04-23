from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountXpRatioMessage(NetworkMessage):
    ratio:int
    

    def init(self, ratio_:int):
        self.ratio = ratio_
        
        super().__init__()
    
    
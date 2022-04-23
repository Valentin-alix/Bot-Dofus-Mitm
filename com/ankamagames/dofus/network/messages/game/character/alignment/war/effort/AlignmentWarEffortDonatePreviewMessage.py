from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonatePreviewMessage(NetworkMessage):
    xp:int
    

    def init(self, xp_:int):
        self.xp = xp_
        
        super().__init__()
    
    
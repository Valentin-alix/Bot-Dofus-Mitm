from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonateRequestMessage(NetworkMessage):
    donation:int
    

    def init(self, donation_:int):
        self.donation = donation_
        
        super().__init__()
    
    
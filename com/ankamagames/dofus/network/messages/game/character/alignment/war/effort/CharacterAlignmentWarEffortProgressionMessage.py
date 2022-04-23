from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterAlignmentWarEffortProgressionMessage(NetworkMessage):
    alignmentWarEffortDailyLimit:int
    alignmentWarEffortDailyDonation:int
    alignmentWarEffortPersonalDonation:int
    

    def init(self, alignmentWarEffortDailyLimit_:int, alignmentWarEffortDailyDonation_:int, alignmentWarEffortPersonalDonation_:int):
        self.alignmentWarEffortDailyLimit = alignmentWarEffortDailyLimit_
        self.alignmentWarEffortDailyDonation = alignmentWarEffortDailyDonation_
        self.alignmentWarEffortPersonalDonation = alignmentWarEffortPersonalDonation_
        
        super().__init__()
    
    
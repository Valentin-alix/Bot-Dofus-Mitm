from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlignmentWarEffortInformation(NetworkMessage):
    alignmentSide:int
    alignmentWarEffort:int
    

    def init(self, alignmentSide_:int, alignmentWarEffort_:int):
        self.alignmentSide = alignmentSide_
        self.alignmentWarEffort = alignmentWarEffort_
        
        super().__init__()
    
    
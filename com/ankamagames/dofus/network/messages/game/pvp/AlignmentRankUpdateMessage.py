from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlignmentRankUpdateMessage(NetworkMessage):
    alignmentRank:int
    verbose:bool
    

    def init(self, alignmentRank_:int, verbose_:bool):
        self.alignmentRank = alignmentRank_
        self.verbose = verbose_
        
        super().__init__()
    
    
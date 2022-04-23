from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ArenaRanking(NetworkMessage):
    rank:int
    bestRank:int
    

    def init(self, rank_:int, bestRank_:int):
        self.rank = rank_
        self.bestRank = bestRank_
        
        super().__init__()
    
    
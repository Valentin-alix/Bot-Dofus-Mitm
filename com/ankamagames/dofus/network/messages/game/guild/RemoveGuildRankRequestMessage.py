from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RemoveGuildRankRequestMessage(NetworkMessage):
    rankId:int
    newRankId:int
    

    def init(self, rankId_:int, newRankId_:int):
        self.rankId = rankId_
        self.newRankId = newRankId_
        
        super().__init__()
    
    
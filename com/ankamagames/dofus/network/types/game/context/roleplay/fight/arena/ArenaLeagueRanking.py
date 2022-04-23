from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ArenaLeagueRanking(NetworkMessage):
    rank:int
    leagueId:int
    leaguePoints:int
    totalLeaguePoints:int
    ladderPosition:int
    

    def init(self, rank_:int, leagueId_:int, leaguePoints_:int, totalLeaguePoints_:int, ladderPosition_:int):
        self.rank = rank_
        self.leagueId = leagueId_
        self.leaguePoints = leaguePoints_
        self.totalLeaguePoints = totalLeaguePoints_
        self.ladderPosition = ladderPosition_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaLeagueRewardsMessage(NetworkMessage):
    seasonId:int
    leagueId:int
    ladderPosition:int
    endSeasonReward:bool
    

    def init(self, seasonId_:int, leagueId_:int, ladderPosition_:int, endSeasonReward_:bool):
        self.seasonId = seasonId_
        self.leagueId = leagueId_
        self.ladderPosition = ladderPosition_
        self.endSeasonReward = endSeasonReward_
        
        super().__init__()
    
    
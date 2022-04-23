from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRanking import ArenaRanking
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaLeagueRanking import ArenaLeagueRanking
    


class ArenaRankInfos(NetworkMessage):
    ranking:'ArenaRanking'
    leagueRanking:'ArenaLeagueRanking'
    victoryCount:int
    fightcount:int
    numFightNeededForLadder:int
    

    def init(self, ranking_:'ArenaRanking', leagueRanking_:'ArenaLeagueRanking', victoryCount_:int, fightcount_:int, numFightNeededForLadder_:int):
        self.ranking = ranking_
        self.leagueRanking = leagueRanking_
        self.victoryCount = victoryCount_
        self.fightcount = fightcount_
        self.numFightNeededForLadder = numFightNeededForLadder_
        
        super().__init__()
    
    
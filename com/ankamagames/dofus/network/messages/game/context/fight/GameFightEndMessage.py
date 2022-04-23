from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
    


class GameFightEndMessage(NetworkMessage):
    duration:int
    rewardRate:int
    lootShareLimitMalus:int
    results:list['FightResultListEntry']
    namedPartyTeamsOutcomes:list['NamedPartyTeamWithOutcome']
    

    def init(self, duration_:int, rewardRate_:int, lootShareLimitMalus_:int, results_:list['FightResultListEntry'], namedPartyTeamsOutcomes_:list['NamedPartyTeamWithOutcome']):
        self.duration = duration_
        self.rewardRate = rewardRate_
        self.lootShareLimitMalus = lootShareLimitMalus_
        self.results = results_
        self.namedPartyTeamsOutcomes = namedPartyTeamsOutcomes_
        
        super().__init__()
    
    
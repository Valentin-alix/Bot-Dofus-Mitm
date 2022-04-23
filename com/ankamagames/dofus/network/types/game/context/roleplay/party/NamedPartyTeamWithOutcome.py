from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam
    


class NamedPartyTeamWithOutcome(NetworkMessage):
    team:'NamedPartyTeam'
    outcome:int
    

    def init(self, team_:'NamedPartyTeam', outcome_:int):
        self.team = team_
        self.outcome = outcome_
        
        super().__init__()
    
    
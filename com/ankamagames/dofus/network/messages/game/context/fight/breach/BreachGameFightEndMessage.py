from com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import GameFightEndMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
    


class BreachGameFightEndMessage(GameFightEndMessage):
    budget:int
    

    def init(self, budget_:int, duration_:int, rewardRate_:int, lootShareLimitMalus_:int, results_:list['FightResultListEntry'], namedPartyTeamsOutcomes_:list['NamedPartyTeamWithOutcome']):
        self.budget = budget_
        
        super().__init__(duration_, rewardRate_, lootShareLimitMalus_, results_, namedPartyTeamsOutcomes_)
    
    
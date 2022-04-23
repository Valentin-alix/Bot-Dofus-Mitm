from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
    


class GameFightUpdateTeamMessage(NetworkMessage):
    fightId:int
    team:'FightTeamInformations'
    

    def init(self, fightId_:int, team_:'FightTeamInformations'):
        self.fightId = fightId_
        self.team = team_
        
        super().__init__()
    
    
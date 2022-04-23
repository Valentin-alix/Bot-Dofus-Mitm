from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations
    


class FightCommonInformations(NetworkMessage):
    fightId:int
    fightType:int
    fightTeams:list['FightTeamInformations']
    fightTeamsPositions:list[int]
    fightTeamsOptions:list['FightOptionsInformations']
    

    def init(self, fightId_:int, fightType_:int, fightTeams_:list['FightTeamInformations'], fightTeamsPositions_:list[int], fightTeamsOptions_:list['FightOptionsInformations']):
        self.fightId = fightId_
        self.fightType = fightType_
        self.fightTeams = fightTeams_
        self.fightTeamsPositions = fightTeamsPositions_
        self.fightTeamsOptions = fightTeamsOptions_
        
        super().__init__()
    
    
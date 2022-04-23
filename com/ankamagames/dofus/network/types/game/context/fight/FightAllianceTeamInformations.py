from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations
    


class FightAllianceTeamInformations(FightTeamInformations):
    relation:int
    

    def init(self, relation_:int, teamMembers_:list['FightTeamMemberInformations'], teamId_:int, leaderId_:int, teamSide_:int, teamTypeId_:int, nbWaves_:int):
        self.relation = relation_
        
        super().__init__(teamMembers_, teamId_, leaderId_, teamSide_, teamTypeId_, nbWaves_)
    
    
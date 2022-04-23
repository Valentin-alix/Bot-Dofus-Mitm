from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations
    


class FightTeamInformations(AbstractFightTeamInformations):
    teamMembers:list['FightTeamMemberInformations']
    

    def init(self, teamMembers_:list['FightTeamMemberInformations'], teamId_:int, leaderId_:int, teamSide_:int, teamTypeId_:int, nbWaves_:int):
        self.teamMembers = teamMembers_
        
        super().__init__(teamId_, leaderId_, teamSide_, teamTypeId_, nbWaves_)
    
    
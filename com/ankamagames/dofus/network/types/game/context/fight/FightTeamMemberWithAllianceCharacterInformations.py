from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
    


class FightTeamMemberWithAllianceCharacterInformations(FightTeamMemberCharacterInformations):
    allianceInfos:'BasicAllianceInformations'
    

    def init(self, allianceInfos_:'BasicAllianceInformations', name_:str, level_:int, id_:int):
        self.allianceInfos = allianceInfos_
        
        super().__init__(name_, level_, id_)
    
    
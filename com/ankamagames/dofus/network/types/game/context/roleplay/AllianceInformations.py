from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceInformations(BasicNamedAllianceInformations):
    allianceEmblem:'GuildEmblem'
    

    def init(self, allianceEmblem_:'GuildEmblem', allianceName_:str, allianceId_:int, allianceTag_:str):
        self.allianceEmblem = allianceEmblem_
        
        super().__init__(allianceName_, allianceId_, allianceTag_)
    
    
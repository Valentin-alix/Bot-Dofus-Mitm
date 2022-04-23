from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AlliancedGuildFactSheetInformations(GuildInformations):
    allianceInfos:'BasicNamedAllianceInformations'
    

    def init(self, allianceInfos_:'BasicNamedAllianceInformations', guildEmblem_:'GuildEmblem', guildId_:int, guildName_:str, guildLevel_:int):
        self.allianceInfos = allianceInfos_
        
        super().__init__(guildEmblem_, guildId_, guildName_, guildLevel_)
    
    
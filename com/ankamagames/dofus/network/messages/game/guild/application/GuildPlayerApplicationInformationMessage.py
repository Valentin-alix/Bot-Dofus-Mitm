from com.ankamagames.dofus.network.messages.game.guild.application.GuildPlayerApplicationAbstractMessage import GuildPlayerApplicationAbstractMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation
    


class GuildPlayerApplicationInformationMessage(GuildPlayerApplicationAbstractMessage):
    guildInformation:'GuildInformations'
    apply:'GuildApplicationInformation'
    

    def init(self, guildInformation_:'GuildInformations', apply_:'GuildApplicationInformation'):
        self.guildInformation = guildInformation_
        self.apply = apply_
        
        super().__init__()
    
    
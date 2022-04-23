from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class HumanOptionGuild(HumanOption):
    guildInformations:'GuildInformations'
    

    def init(self, guildInformations_:'GuildInformations'):
        self.guildInformations = guildInformations_
        
        super().__init__()
    
    
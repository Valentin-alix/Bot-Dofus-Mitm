from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class TaxCollectorGuildInformations(TaxCollectorComplementaryInformations):
    guild:'BasicGuildInformations'
    

    def init(self, guild_:'BasicGuildInformations'):
        self.guild = guild_
        
        super().__init__()
    
    
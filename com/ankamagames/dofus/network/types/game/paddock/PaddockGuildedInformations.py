from com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class PaddockGuildedInformations(PaddockBuyableInformations):
    deserted:bool
    guildInfo:'GuildInformations'
    

    def init(self, deserted_:bool, guildInfo_:'GuildInformations', price_:int, locked_:bool):
        self.deserted = deserted_
        self.guildInfo = guildInfo_
        
        super().__init__(price_, locked_)
    
    
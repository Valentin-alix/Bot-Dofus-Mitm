from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations
    


class TopTaxCollectorListMessage(AbstractTaxCollectorListMessage):
    isDungeon:bool
    

    def init(self, isDungeon_:bool, informations_:list['TaxCollectorInformations']):
        self.isDungeon = isDungeon_
        
        super().__init__(informations_)
    
    
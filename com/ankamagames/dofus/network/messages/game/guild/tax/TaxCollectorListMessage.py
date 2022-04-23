from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorFightersInformation import TaxCollectorFightersInformation
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations
    


class TaxCollectorListMessage(AbstractTaxCollectorListMessage):
    nbcollectorMax:int
    fightersInformations:list['TaxCollectorFightersInformation']
    infoType:int
    

    def init(self, nbcollectorMax_:int, fightersInformations_:list['TaxCollectorFightersInformation'], infoType_:int, informations_:list['TaxCollectorInformations']):
        self.nbcollectorMax = nbcollectorMax_
        self.fightersInformations = fightersInformations_
        self.infoType = infoType_
        
        super().__init__(informations_)
    
    
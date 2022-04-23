from com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations
    


class PaddockInstancesInformations(PaddockInformations):
    paddocks:list['PaddockBuyableInformations']
    

    def init(self, paddocks_:list['PaddockBuyableInformations'], maxOutdoorMount_:int, maxItems_:int):
        self.paddocks = paddocks_
        
        super().__init__(maxOutdoorMount_, maxItems_)
    
    
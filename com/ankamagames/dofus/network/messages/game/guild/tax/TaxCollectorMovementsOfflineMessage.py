from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorMovement import TaxCollectorMovement
    


class TaxCollectorMovementsOfflineMessage(NetworkMessage):
    movements:list['TaxCollectorMovement']
    

    def init(self, movements_:list['TaxCollectorMovement']):
        self.movements = movements_
        
        super().__init__()
    
    
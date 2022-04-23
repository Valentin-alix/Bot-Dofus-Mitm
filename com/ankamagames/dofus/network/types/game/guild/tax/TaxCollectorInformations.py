from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
    


class TaxCollectorInformations(NetworkMessage):
    uniqueId:int
    firtNameId:int
    lastNameId:int
    additionalInfos:'AdditionalTaxCollectorInformations'
    worldX:int
    worldY:int
    subAreaId:int
    state:int
    look:'EntityLook'
    complements:list['TaxCollectorComplementaryInformations']
    

    def init(self, uniqueId_:int, firtNameId_:int, lastNameId_:int, additionalInfos_:'AdditionalTaxCollectorInformations', worldX_:int, worldY_:int, subAreaId_:int, state_:int, look_:'EntityLook', complements_:list['TaxCollectorComplementaryInformations']):
        self.uniqueId = uniqueId_
        self.firtNameId = firtNameId_
        self.lastNameId = lastNameId_
        self.additionalInfos = additionalInfos_
        self.worldX = worldX_
        self.worldY = worldY_
        self.subAreaId = subAreaId_
        self.state = state_
        self.look = look_
        self.complements = complements_
        
        super().__init__()
    
    
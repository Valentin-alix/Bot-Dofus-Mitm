from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMountWithOutPaddockMessage import ExchangeStartOkMountWithOutPaddockMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
    from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
    


class ExchangeStartOkMountMessage(ExchangeStartOkMountWithOutPaddockMessage):
    paddockedMountsDescription:list['MountClientData']
    

    def init(self, paddockedMountsDescription_:list['MountClientData'], stabledMountsDescription_:list['MountClientData']):
        self.paddockedMountsDescription = paddockedMountsDescription_
        
        super().__init__(stabledMountsDescription_)
    
    
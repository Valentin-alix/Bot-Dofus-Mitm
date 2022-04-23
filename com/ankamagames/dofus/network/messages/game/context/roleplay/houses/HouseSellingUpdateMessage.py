from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class HouseSellingUpdateMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    realPrice:int
    buyerTag:'AccountTagInformation'
    

    def init(self, houseId_:int, instanceId_:int, secondHand_:bool, realPrice_:int, buyerTag_:'AccountTagInformation'):
        self.houseId = houseId_
        self.instanceId = instanceId_
        self.secondHand = secondHand_
        self.realPrice = realPrice_
        self.buyerTag = buyerTag_
        
        super().__init__()
    
    
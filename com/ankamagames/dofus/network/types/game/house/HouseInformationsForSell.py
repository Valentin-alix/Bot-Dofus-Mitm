from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class HouseInformationsForSell(NetworkMessage):
    instanceId:int
    secondHand:bool
    modelId:int
    ownerTag:'AccountTagInformation'
    hasOwner:bool
    ownerCharacterName:str
    worldX:int
    worldY:int
    subAreaId:int
    nbRoom:int
    nbChest:int
    skillListIds:list[int]
    isLocked:bool
    price:int
    

    def init(self, instanceId_:int, secondHand_:bool, modelId_:int, ownerTag_:'AccountTagInformation', hasOwner_:bool, ownerCharacterName_:str, worldX_:int, worldY_:int, subAreaId_:int, nbRoom_:int, nbChest_:int, skillListIds_:list[int], isLocked_:bool, price_:int):
        self.instanceId = instanceId_
        self.secondHand = secondHand_
        self.modelId = modelId_
        self.ownerTag = ownerTag_
        self.hasOwner = hasOwner_
        self.ownerCharacterName = ownerCharacterName_
        self.worldX = worldX_
        self.worldY = worldY_
        self.subAreaId = subAreaId_
        self.nbRoom = nbRoom_
        self.nbChest = nbChest_
        self.skillListIds = skillListIds_
        self.isLocked = isLocked_
        self.price = price_
        
        super().__init__()
    
    
from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class HouseInformationsForGuild(HouseInformations):
    instanceId:int
    secondHand:bool
    ownerTag:'AccountTagInformation'
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    skillListIds:list[int]
    guildshareParams:int
    

    def init(self, instanceId_:int, secondHand_:bool, ownerTag_:'AccountTagInformation', worldX_:int, worldY_:int, mapId_:int, subAreaId_:int, skillListIds_:list[int], guildshareParams_:int, houseId_:int, modelId_:int):
        self.instanceId = instanceId_
        self.secondHand = secondHand_
        self.ownerTag = ownerTag_
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        self.skillListIds = skillListIds_
        self.guildshareParams = guildshareParams_
        
        super().__init__(houseId_, modelId_)
    
    
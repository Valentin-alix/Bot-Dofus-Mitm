from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class AllianceInsiderPrismInformation(PrismInformation):
    lastTimeSlotModificationDate:int
    lastTimeSlotModificationAuthorGuildId:int
    lastTimeSlotModificationAuthorId:int
    lastTimeSlotModificationAuthorName:str
    modulesObjects:list['ObjectItem']
    

    def init(self, lastTimeSlotModificationDate_:int, lastTimeSlotModificationAuthorGuildId_:int, lastTimeSlotModificationAuthorId_:int, lastTimeSlotModificationAuthorName_:str, modulesObjects_:list['ObjectItem'], typeId_:int, state_:int, nextVulnerabilityDate_:int, placementDate_:int, rewardTokenCount_:int):
        self.lastTimeSlotModificationDate = lastTimeSlotModificationDate_
        self.lastTimeSlotModificationAuthorGuildId = lastTimeSlotModificationAuthorGuildId_
        self.lastTimeSlotModificationAuthorId = lastTimeSlotModificationAuthorId_
        self.lastTimeSlotModificationAuthorName = lastTimeSlotModificationAuthorName_
        self.modulesObjects = modulesObjects_
        
        super().__init__(typeId_, state_, nextVulnerabilityDate_, placementDate_, rewardTokenCount_)
    
    
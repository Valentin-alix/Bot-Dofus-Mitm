from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
    


class ExchangeGuildTaxCollectorGetMessage(NetworkMessage):
    collectorName:str
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    userName:str
    callerId:int
    callerName:str
    experience:int
    pods:int
    objectsInfos:list['ObjectItemGenericQuantity']
    

    def init(self, collectorName_:str, worldX_:int, worldY_:int, mapId_:int, subAreaId_:int, userName_:str, callerId_:int, callerName_:str, experience_:int, pods_:int, objectsInfos_:list['ObjectItemGenericQuantity']):
        self.collectorName = collectorName_
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        self.userName = userName_
        self.callerId = callerId_
        self.callerName = callerName_
        self.experience = experience_
        self.pods = pods_
        self.objectsInfos = objectsInfos_
        
        super().__init__()
    
    
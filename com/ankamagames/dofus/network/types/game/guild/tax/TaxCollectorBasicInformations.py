from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TaxCollectorBasicInformations(NetworkMessage):
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    

    def init(self, firstNameId_:int, lastNameId_:int, worldX_:int, worldY_:int, mapId_:int, subAreaId_:int):
        self.firstNameId = firstNameId_
        self.lastNameId = lastNameId_
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        
        super().__init__()
    
    
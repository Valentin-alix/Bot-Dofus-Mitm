from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PartyMemberGeoPosition(NetworkMessage):
    memberId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    

    def init(self, memberId_:int, worldX_:int, worldY_:int, mapId_:int, subAreaId_:int):
        self.memberId = memberId_
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        
        super().__init__()
    
    
from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates


class MapCoordinatesAndId(MapCoordinates):
    mapId:int
    

    def init(self, mapId_:int, worldX_:int, worldY_:int):
        self.mapId = mapId_
        
        super().__init__(worldX_, worldY_)
    
    
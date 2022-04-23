from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapCoordinates(NetworkMessage):
    worldX:int
    worldY:int
    

    def init(self, worldX_:int, worldY_:int):
        self.worldX = worldX_
        self.worldY = worldY_
        
        super().__init__()
    
    
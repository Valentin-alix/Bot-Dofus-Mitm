from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountFreeFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    liberator:str
    

    def init(self, name_:str, worldX_:int, worldY_:int, liberator_:str):
        self.name = name_
        self.worldX = worldX_
        self.worldY = worldY_
        self.liberator = liberator_
        
        super().__init__()
    
    
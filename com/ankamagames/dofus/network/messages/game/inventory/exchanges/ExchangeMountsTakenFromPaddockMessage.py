from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountsTakenFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    ownername:str
    

    def init(self, name_:str, worldX_:int, worldY_:int, ownername_:str):
        self.name = name_
        self.worldX = worldX_
        self.worldY = worldY_
        self.ownername = ownername_
        
        super().__init__()
    
    
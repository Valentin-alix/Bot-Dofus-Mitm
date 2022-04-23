from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountSterilizeFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    sterilizator:str
    

    def init(self, name_:str, worldX_:int, worldY_:int, sterilizator_:str):
        self.name = name_
        self.worldX = worldX_
        self.worldY = worldY_
        self.sterilizator = sterilizator_
        
        super().__init__()
    
    
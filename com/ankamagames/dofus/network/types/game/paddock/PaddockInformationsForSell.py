from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockInformationsForSell(NetworkMessage):
    guildOwner:str
    worldX:int
    worldY:int
    subAreaId:int
    nbMount:int
    nbObject:int
    price:int
    

    def init(self, guildOwner_:str, worldX_:int, worldY_:int, subAreaId_:int, nbMount_:int, nbObject_:int, price_:int):
        self.guildOwner = guildOwner_
        self.worldX = worldX_
        self.worldY = worldY_
        self.subAreaId = subAreaId_
        self.nbMount = nbMount_
        self.nbObject = nbObject_
        self.price = price_
        
        super().__init__()
    
    
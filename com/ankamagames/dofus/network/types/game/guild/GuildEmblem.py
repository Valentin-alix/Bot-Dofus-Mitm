from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildEmblem(NetworkMessage):
    symbolShape:int
    symbolColor:int
    backgroundShape:int
    backgroundColor:int
    

    def init(self, symbolShape_:int, symbolColor_:int, backgroundShape_:int, backgroundColor_:int):
        self.symbolShape = symbolShape_
        self.symbolColor = symbolColor_
        self.backgroundShape = backgroundShape_
        self.backgroundColor = backgroundColor_
        
        super().__init__()
    
    
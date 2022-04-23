from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCapabilitiesMessage(NetworkMessage):
    guildEmblemSymbolCategories:int
    

    def init(self, guildEmblemSymbolCategories_:int):
        self.guildEmblemSymbolCategories = guildEmblemSymbolCategories_
        
        super().__init__()
    
    
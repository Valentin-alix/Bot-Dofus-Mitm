from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InvalidPresetsMessage(NetworkMessage):
    presetIds:list[int]
    

    def init(self, presetIds_:list[int]):
        self.presetIds = presetIds_
        
        super().__init__()
    
    
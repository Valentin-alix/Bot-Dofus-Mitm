from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SimpleCharacterCharacteristicForPreset(NetworkMessage):
    keyword:str
    base:int
    additionnal:int
    

    def init(self, keyword_:str, base_:int, additionnal_:int):
        self.keyword = keyword_
        self.base = base_
        self.additionnal = additionnal_
        
        super().__init__()
    
    
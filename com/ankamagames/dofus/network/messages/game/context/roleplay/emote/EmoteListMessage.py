from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EmoteListMessage(NetworkMessage):
    emoteIds:list[int]
    

    def init(self, emoteIds_:list[int]):
        self.emoteIds = emoteIds_
        
        super().__init__()
    
    
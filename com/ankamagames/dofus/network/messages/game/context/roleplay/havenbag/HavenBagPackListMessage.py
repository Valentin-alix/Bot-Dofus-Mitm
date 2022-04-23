from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagPackListMessage(NetworkMessage):
    packIds:list[int]
    

    def init(self, packIds_:list[int]):
        self.packIds = packIds_
        
        super().__init__()
    
    
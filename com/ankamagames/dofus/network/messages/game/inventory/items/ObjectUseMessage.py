from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectUseMessage(NetworkMessage):
    objectUID:int
    

    def init(self, objectUID_:int):
        self.objectUID = objectUID_
        
        super().__init__()
    
    
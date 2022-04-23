from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectsDeletedMessage(NetworkMessage):
    objectUID:list[int]
    

    def init(self, objectUID_:list[int]):
        self.objectUID = objectUID_
        
        super().__init__()
    
    
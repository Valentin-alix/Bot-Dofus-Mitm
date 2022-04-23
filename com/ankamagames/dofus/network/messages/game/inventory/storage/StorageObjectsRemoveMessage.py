from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StorageObjectsRemoveMessage(NetworkMessage):
    objectUIDList:list[int]
    

    def init(self, objectUIDList_:list[int]):
        self.objectUIDList = objectUIDList_
        
        super().__init__()
    
    
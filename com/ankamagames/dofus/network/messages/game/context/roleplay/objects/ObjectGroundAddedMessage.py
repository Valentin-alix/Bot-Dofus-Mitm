from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectGroundAddedMessage(NetworkMessage):
    cellId:int
    objectGID:int
    

    def init(self, cellId_:int, objectGID_:int):
        self.cellId = cellId_
        self.objectGID = objectGID_
        
        super().__init__()
    
    
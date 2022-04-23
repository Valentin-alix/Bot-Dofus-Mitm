from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectMovementMessage(NetworkMessage):
    objectUID:int
    position:int
    

    def init(self, objectUID_:int, position_:int):
        self.objectUID = objectUID_
        self.position = position_
        
        super().__init__()
    
    
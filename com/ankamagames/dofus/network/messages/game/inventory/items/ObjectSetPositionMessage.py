from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectSetPositionMessage(NetworkMessage):
    objectUID:int
    position:int
    quantity:int
    

    def init(self, objectUID_:int, position_:int, quantity_:int):
        self.objectUID = objectUID_
        self.position = position_
        self.quantity = quantity_
        
        super().__init__()
    
    
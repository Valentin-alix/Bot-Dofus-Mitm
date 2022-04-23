from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectQuantityMessage(NetworkMessage):
    objectUID:int
    quantity:int
    origin:int
    

    def init(self, objectUID_:int, quantity_:int, origin_:int):
        self.objectUID = objectUID_
        self.quantity = quantity_
        self.origin = origin_
        
        super().__init__()
    
    
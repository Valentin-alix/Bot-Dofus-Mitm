from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectDropMessage(NetworkMessage):
    objectUID:int
    quantity:int
    

    def init(self, objectUID_:int, quantity_:int):
        self.objectUID = objectUID_
        self.quantity = quantity_
        
        super().__init__()
    
    
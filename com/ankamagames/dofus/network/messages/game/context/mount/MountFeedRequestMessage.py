from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountFeedRequestMessage(NetworkMessage):
    mountUid:int
    mountLocation:int
    mountFoodUid:int
    quantity:int
    

    def init(self, mountUid_:int, mountLocation_:int, mountFoodUid_:int, quantity_:int):
        self.mountUid = mountUid_
        self.mountLocation = mountLocation_
        self.mountFoodUid = mountFoodUid_
        self.quantity = quantity_
        
        super().__init__()
    
    
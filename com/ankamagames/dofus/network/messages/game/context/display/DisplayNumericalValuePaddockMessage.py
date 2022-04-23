from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DisplayNumericalValuePaddockMessage(NetworkMessage):
    rideId:int
    value:int
    type:int
    

    def init(self, rideId_:int, value_:int, type_:int):
        self.rideId = rideId_
        self.value = value_
        self.type = type_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountInformationInPaddockRequestMessage(NetworkMessage):
    mapRideId:int
    

    def init(self, mapRideId_:int):
        self.mapRideId = mapRideId_
        
        super().__init__()
    
    
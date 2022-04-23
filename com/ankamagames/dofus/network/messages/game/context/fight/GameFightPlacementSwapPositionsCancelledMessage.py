from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsCancelledMessage(NetworkMessage):
    requestId:int
    cancellerId:int
    

    def init(self, requestId_:int, cancellerId_:int):
        self.requestId = requestId_
        self.cancellerId = cancellerId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsCancelMessage(NetworkMessage):
    requestId:int
    

    def init(self, requestId_:int):
        self.requestId = requestId_
        
        super().__init__()
    
    
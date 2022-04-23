from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsOfferMessage(NetworkMessage):
    requestId:int
    requesterId:int
    requesterCellId:int
    requestedId:int
    requestedCellId:int
    

    def init(self, requestId_:int, requesterId_:int, requesterCellId_:int, requestedId_:int, requestedCellId_:int):
        self.requestId = requestId_
        self.requesterId = requesterId_
        self.requesterCellId = requesterCellId_
        self.requestedId = requestedId_
        self.requestedCellId = requestedCellId_
        
        super().__init__()
    
    
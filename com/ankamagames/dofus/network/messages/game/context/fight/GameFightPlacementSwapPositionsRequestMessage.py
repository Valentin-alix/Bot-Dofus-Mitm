from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementPositionRequestMessage import GameFightPlacementPositionRequestMessage


class GameFightPlacementSwapPositionsRequestMessage(GameFightPlacementPositionRequestMessage):
    requestedId:int
    

    def init(self, requestedId_:int, cellId_:int):
        self.requestedId = requestedId_
        
        super().__init__(cellId_)
    
    
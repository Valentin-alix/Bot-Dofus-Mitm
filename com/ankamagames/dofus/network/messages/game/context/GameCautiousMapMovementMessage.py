from com.ankamagames.dofus.network.messages.game.context.GameMapMovementMessage import GameMapMovementMessage


class GameCautiousMapMovementMessage(GameMapMovementMessage):
    

    def init(self, keyMovements_:list[int], forcedDirection_:int, actorId_:int):
        
        super().__init__(keyMovements_, forcedDirection_, actorId_)
    
    
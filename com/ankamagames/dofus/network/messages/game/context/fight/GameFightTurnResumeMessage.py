from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartMessage import GameFightTurnStartMessage


class GameFightTurnResumeMessage(GameFightTurnStartMessage):
    remainingTime:int
    

    def init(self, remainingTime_:int, id_:int, waitTime_:int):
        self.remainingTime = remainingTime_
        
        super().__init__(id_, waitTime_)
    
    
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSlideMessage(AbstractGameActionMessage):
    targetId:int
    startCellId:int
    endCellId:int
    

    def init(self, targetId_:int, startCellId_:int, endCellId_:int, actionId_:int, sourceId_:int):
        self.targetId = targetId_
        self.startCellId = startCellId_
        self.endCellId = endCellId_
        
        super().__init__(actionId_, sourceId_)
    
    
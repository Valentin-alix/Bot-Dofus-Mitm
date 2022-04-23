from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightUnmarkCellsMessage(AbstractGameActionMessage):
    markId:int
    

    def init(self, markId_:int, actionId_:int, sourceId_:int):
        self.markId = markId_
        
        super().__init__(actionId_, sourceId_)
    
    
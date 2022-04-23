from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionWithAckMessage(AbstractGameActionMessage):
    waitAckId:int
    

    def init(self, waitAckId_:int, actionId_:int, sourceId_:int):
        self.waitAckId = waitAckId_
        
        super().__init__(actionId_, sourceId_)
    
    
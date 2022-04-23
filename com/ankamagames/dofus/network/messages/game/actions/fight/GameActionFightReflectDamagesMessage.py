from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightReflectDamagesMessage(AbstractGameActionMessage):
    targetId:int
    

    def init(self, targetId_:int, actionId_:int, sourceId_:int):
        self.targetId = targetId_
        
        super().__init__(actionId_, sourceId_)
    
    
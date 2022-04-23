from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightModifyEffectsDurationMessage(AbstractGameActionMessage):
    targetId:int
    delta:int
    

    def init(self, targetId_:int, delta_:int, actionId_:int, sourceId_:int):
        self.targetId = targetId_
        self.delta = delta_
        
        super().__init__(actionId_, sourceId_)
    
    
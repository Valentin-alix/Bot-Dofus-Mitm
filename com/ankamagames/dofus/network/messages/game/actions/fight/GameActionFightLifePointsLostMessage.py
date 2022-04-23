from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightLifePointsLostMessage(AbstractGameActionMessage):
    targetId:int
    loss:int
    permanentDamages:int
    elementId:int
    

    def init(self, targetId_:int, loss_:int, permanentDamages_:int, elementId_:int, actionId_:int, sourceId_:int):
        self.targetId = targetId_
        self.loss = loss_
        self.permanentDamages = permanentDamages_
        self.elementId = elementId_
        
        super().__init__(actionId_, sourceId_)
    
    
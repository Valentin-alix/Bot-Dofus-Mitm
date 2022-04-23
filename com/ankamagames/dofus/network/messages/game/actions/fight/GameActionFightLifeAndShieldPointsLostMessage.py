from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightLifePointsLostMessage import GameActionFightLifePointsLostMessage


class GameActionFightLifeAndShieldPointsLostMessage(GameActionFightLifePointsLostMessage):
    shieldLoss:int
    

    def init(self, shieldLoss_:int, targetId_:int, loss_:int, permanentDamages_:int, elementId_:int, actionId_:int, sourceId_:int):
        self.shieldLoss = shieldLoss_
        
        super().__init__(targetId_, loss_, permanentDamages_, elementId_, actionId_, sourceId_)
    
    
from com.ankamagames.dofus.network.messages.game.character.stats.UpdateLifePointsMessage import UpdateLifePointsMessage


class LifePointsRegenEndMessage(UpdateLifePointsMessage):
    lifePointsGained:int
    

    def init(self, lifePointsGained_:int, lifePoints_:int, maxLifePoints_:int):
        self.lifePointsGained = lifePointsGained_
        
        super().__init__(lifePoints_, maxLifePoints_)
    
    
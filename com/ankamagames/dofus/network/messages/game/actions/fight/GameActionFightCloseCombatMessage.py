from com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightCloseCombatMessage(AbstractGameActionFightTargetedAbilityMessage):
    weaponGenericId:int
    

    def init(self, weaponGenericId_:int, targetId_:int, destinationCellId_:int, critical_:int, silentCast_:bool, verboseCast_:bool, actionId_:int, sourceId_:int):
        self.weaponGenericId = weaponGenericId_
        
        super().__init__(targetId_, destinationCellId_, critical_, silentCast_, verboseCast_, actionId_, sourceId_)
    
    
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionFightTargetedAbilityMessage(AbstractGameActionMessage):
    targetId:int
    destinationCellId:int
    critical:int
    silentCast:bool
    verboseCast:bool
    silentCast:bool
    verboseCast:bool
    

    def init(self, targetId_:int, destinationCellId_:int, critical_:int, silentCast_:bool, verboseCast_:bool, actionId_:int, sourceId_:int):
        self.targetId = targetId_
        self.destinationCellId = destinationCellId_
        self.critical = critical_
        self.silentCast = silentCast_
        self.verboseCast = verboseCast_
        
        super().__init__(actionId_, sourceId_)
    
    
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDispellMessage(AbstractGameActionMessage):
    targetId:int
    verboseCast:bool
    

    def init(self, targetId_:int, verboseCast_:bool, actionId_:int, sourceId_:int):
        self.targetId = targetId_
        self.verboseCast = verboseCast_
        
        super().__init__(actionId_, sourceId_)
    
    
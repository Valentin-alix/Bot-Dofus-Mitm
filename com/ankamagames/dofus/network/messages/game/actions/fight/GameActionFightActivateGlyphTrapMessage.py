from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightActivateGlyphTrapMessage(AbstractGameActionMessage):
    markId:int
    active:bool
    

    def init(self, markId_:int, active_:bool, actionId_:int, sourceId_:int):
        self.markId = markId_
        self.active = active_
        
        super().__init__(actionId_, sourceId_)
    
    
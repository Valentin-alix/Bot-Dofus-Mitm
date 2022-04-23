from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
    markId:int
    markImpactCell:int
    triggeringCharacterId:int
    triggeredSpellId:int
    

    def init(self, markId_:int, markImpactCell_:int, triggeringCharacterId_:int, triggeredSpellId_:int, actionId_:int, sourceId_:int):
        self.markId = markId_
        self.markImpactCell = markImpactCell_
        self.triggeringCharacterId = triggeringCharacterId_
        self.triggeredSpellId = triggeredSpellId_
        
        super().__init__(actionId_, sourceId_)
    
    
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
    targetId:int
    spellId:int
    value:int
    

    def init(self, targetId_:int, spellId_:int, value_:int, actionId_:int, sourceId_:int):
        self.targetId = targetId_
        self.spellId = spellId_
        self.value = value_
        
        super().__init__(actionId_, sourceId_)
    
    
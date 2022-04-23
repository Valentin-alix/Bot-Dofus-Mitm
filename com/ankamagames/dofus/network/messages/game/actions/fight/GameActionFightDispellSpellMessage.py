from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellMessage import GameActionFightDispellMessage


class GameActionFightDispellSpellMessage(GameActionFightDispellMessage):
    spellId:int
    

    def init(self, spellId_:int, targetId_:int, verboseCast_:bool, actionId_:int, sourceId_:int):
        self.spellId = spellId_
        
        super().__init__(targetId_, verboseCast_, actionId_, sourceId_)
    
    
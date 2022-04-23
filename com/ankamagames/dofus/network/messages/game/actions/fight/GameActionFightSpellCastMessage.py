from com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage


class GameActionFightSpellCastMessage(AbstractGameActionFightTargetedAbilityMessage):
    spellId:int
    spellLevel:int
    portalsIds:list[int]
    

    def init(self, spellId_:int, spellLevel_:int, portalsIds_:list[int], targetId_:int, destinationCellId_:int, critical_:int, silentCast_:bool, verboseCast_:bool, actionId_:int, sourceId_:int):
        self.spellId = spellId_
        self.spellLevel = spellLevel_
        self.portalsIds = portalsIds_
        
        super().__init__(targetId_, destinationCellId_, critical_, silentCast_, verboseCast_, actionId_, sourceId_)
    
    
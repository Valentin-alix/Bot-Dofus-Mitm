from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class FightTemporarySpellImmunityEffect(AbstractFightDispellableEffect):
    immuneSpellId:int
    

    def init(self, immuneSpellId_:int, uid_:int, targetId_:int, turnDuration_:int, dispelable_:int, spellId_:int, effectId_:int, parentBoostUid_:int):
        self.immuneSpellId = immuneSpellId_
        
        super().__init__(uid_, targetId_, turnDuration_, dispelable_, spellId_, effectId_, parentBoostUid_)
    
    
from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import FightTemporaryBoostEffect


class FightTemporarySpellBoostEffect(FightTemporaryBoostEffect):
    boostedSpellId:int
    

    def init(self, boostedSpellId_:int, delta_:int, uid_:int, targetId_:int, turnDuration_:int, dispelable_:int, spellId_:int, effectId_:int, parentBoostUid_:int):
        self.boostedSpellId = boostedSpellId_
        
        super().__init__(delta_, uid_, targetId_, turnDuration_, dispelable_, spellId_, effectId_, parentBoostUid_)
    
    
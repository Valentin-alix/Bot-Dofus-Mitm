from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification
    


class UpdateSpellModifierMessage(NetworkMessage):
    actorId:int
    spellModifier:'CharacterSpellModification'
    

    def init(self, actorId_:int, spellModifier_:'CharacterSpellModification'):
        self.actorId = actorId_
        self.spellModifier = spellModifier_
        
        super().__init__()
    
    
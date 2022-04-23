from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
    


class CharacterSpellModification(NetworkMessage):
    modificationType:int
    spellId:int
    value:'CharacterCharacteristicDetailed'
    

    def init(self, modificationType_:int, spellId_:int, value_:'CharacterCharacteristicDetailed'):
        self.modificationType = modificationType_
        self.spellId = spellId_
        self.value = value_
        
        super().__init__()
    
    
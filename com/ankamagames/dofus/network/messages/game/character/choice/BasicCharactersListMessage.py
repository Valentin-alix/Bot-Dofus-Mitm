from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
    


class BasicCharactersListMessage(NetworkMessage):
    characters:list['CharacterBaseInformations']
    

    def init(self, characters_:list['CharacterBaseInformations']):
        self.characters = characters_
        
        super().__init__()
    
    
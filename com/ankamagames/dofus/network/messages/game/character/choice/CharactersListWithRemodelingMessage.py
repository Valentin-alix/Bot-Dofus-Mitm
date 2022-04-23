from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListMessage import CharactersListMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.choice.CharacterToRemodelInformations import CharacterToRemodelInformations
    from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
    


class CharactersListWithRemodelingMessage(CharactersListMessage):
    charactersToRemodel:list['CharacterToRemodelInformations']
    

    def init(self, charactersToRemodel_:list['CharacterToRemodelInformations'], hasStartupActions_:bool, characters_:list['CharacterBaseInformations']):
        self.charactersToRemodel = charactersToRemodel_
        
        super().__init__(hasStartupActions_, characters_)
    
    
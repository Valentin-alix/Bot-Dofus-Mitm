from com.ankamagames.dofus.network.types.game.character.AbstractCharacterInformation import AbstractCharacterInformation


class CharacterBasicMinimalInformations(AbstractCharacterInformation):
    name:str
    

    def init(self, name_:str, id_:int):
        self.name = name_
        
        super().__init__(id_)
    
    
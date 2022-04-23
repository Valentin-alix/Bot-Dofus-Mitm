from com.ankamagames.dofus.network.types.game.character.AbstractCharacterInformation import AbstractCharacterInformation


class CharacterRemodelingInformation(AbstractCharacterInformation):
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:list[int]
    

    def init(self, name_:str, breed_:int, sex_:bool, cosmeticId_:int, colors_:list[int], id_:int):
        self.name = name_
        self.breed = breed_
        self.sex = sex_
        self.cosmeticId = cosmeticId_
        self.colors = colors_
        
        super().__init__(id_)
    
    
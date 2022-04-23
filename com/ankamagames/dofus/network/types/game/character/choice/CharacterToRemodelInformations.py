from com.ankamagames.dofus.network.types.game.character.choice.CharacterRemodelingInformation import CharacterRemodelingInformation


class CharacterToRemodelInformations(CharacterRemodelingInformation):
    possibleChangeMask:int
    mandatoryChangeMask:int
    

    def init(self, possibleChangeMask_:int, mandatoryChangeMask_:int, name_:str, breed_:int, sex_:bool, cosmeticId_:int, colors_:list[int], id_:int):
        self.possibleChangeMask = possibleChangeMask_
        self.mandatoryChangeMask = mandatoryChangeMask_
        
        super().__init__(name_, breed_, sex_, cosmeticId_, colors_, id_)
    
    
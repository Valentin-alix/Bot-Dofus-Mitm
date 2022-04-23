from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed


class CharacterUsableCharacteristicDetailed(CharacterCharacteristicDetailed):
    used:int
    

    def init(self, used_:int, base_:int, additional_:int, objectsAndMountBonus_:int, alignGiftBonus_:int, contextModif_:int, characteristicId_:int):
        self.used = used_
        
        super().__init__(base_, additional_, objectsAndMountBonus_, alignGiftBonus_, contextModif_, characteristicId_)
    
    
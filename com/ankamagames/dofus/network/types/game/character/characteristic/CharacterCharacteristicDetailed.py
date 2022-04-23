from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristicDetailed(CharacterCharacteristic):
    base:int
    additional:int
    objectsAndMountBonus:int
    alignGiftBonus:int
    contextModif:int
    

    def init(self, base_:int, additional_:int, objectsAndMountBonus_:int, alignGiftBonus_:int, contextModif_:int, characteristicId_:int):
        self.base = base_
        self.additional = additional_
        self.objectsAndMountBonus = objectsAndMountBonus_
        self.alignGiftBonus = alignGiftBonus_
        self.contextModif = contextModif_
        
        super().__init__(characteristicId_)
    
    
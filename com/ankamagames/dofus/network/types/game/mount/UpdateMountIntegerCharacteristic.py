from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic


class UpdateMountIntegerCharacteristic(UpdateMountCharacteristic):
    value:int
    

    def init(self, value_:int, type_:int):
        self.value = value_
        
        super().__init__(type_)
    
    
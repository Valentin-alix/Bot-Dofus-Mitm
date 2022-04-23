from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCharacteristic(NetworkMessage):
    characteristicId:int
    

    def init(self, characteristicId_:int):
        self.characteristicId = characteristicId_
        
        super().__init__()
    
    
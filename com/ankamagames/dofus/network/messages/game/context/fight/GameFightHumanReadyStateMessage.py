from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightHumanReadyStateMessage(NetworkMessage):
    characterId:int
    isReady:bool
    

    def init(self, characterId_:int, isReady_:bool):
        self.characterId = characterId_
        self.isReady = isReady_
        
        super().__init__()
    
    
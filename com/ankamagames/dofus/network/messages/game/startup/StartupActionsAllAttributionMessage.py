from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StartupActionsAllAttributionMessage(NetworkMessage):
    characterId:int
    

    def init(self, characterId_:int):
        self.characterId = characterId_
        
        super().__init__()
    
    
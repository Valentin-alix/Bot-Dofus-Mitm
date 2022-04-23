from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StartupActionsObjetAttributionMessage(NetworkMessage):
    actionId:int
    characterId:int
    

    def init(self, actionId_:int, characterId_:int):
        self.actionId = actionId_
        self.characterId = characterId_
        
        super().__init__()
    
    
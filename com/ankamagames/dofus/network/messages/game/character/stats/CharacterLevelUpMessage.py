from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterLevelUpMessage(NetworkMessage):
    newLevel:int
    

    def init(self, newLevel_:int):
        self.newLevel = newLevel_
        
        super().__init__()
    
    
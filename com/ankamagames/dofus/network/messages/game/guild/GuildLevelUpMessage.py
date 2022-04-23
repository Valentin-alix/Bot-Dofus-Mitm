from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildLevelUpMessage(NetworkMessage):
    newLevel:int
    

    def init(self, newLevel_:int):
        self.newLevel = newLevel_
        
        super().__init__()
    
    
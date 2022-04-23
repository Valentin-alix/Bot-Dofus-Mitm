from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFactsErrorMessage(NetworkMessage):
    guildId:int
    

    def init(self, guildId_:int):
        self.guildId = guildId_
        
        super().__init__()
    
    
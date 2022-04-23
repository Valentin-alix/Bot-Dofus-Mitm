from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildUpdateApplicationMessage(NetworkMessage):
    applyText:str
    guildId:int
    

    def init(self, applyText_:str, guildId_:int):
        self.applyText = applyText_
        self.guildId = guildId_
        
        super().__init__()
    
    
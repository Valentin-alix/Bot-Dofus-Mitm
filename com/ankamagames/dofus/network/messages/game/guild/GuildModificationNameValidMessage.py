from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildModificationNameValidMessage(NetworkMessage):
    guildName:str
    

    def init(self, guildName_:str):
        self.guildName = guildName_
        
        super().__init__()
    
    
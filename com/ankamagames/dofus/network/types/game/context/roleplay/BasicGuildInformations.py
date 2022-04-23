from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


class BasicGuildInformations(AbstractSocialGroupInfos):
    guildId:int
    guildName:str
    guildLevel:int
    

    def init(self, guildId_:int, guildName_:str, guildLevel_:int):
        self.guildId = guildId_
        self.guildName = guildName_
        self.guildLevel = guildLevel_
        
        super().__init__()
    
    
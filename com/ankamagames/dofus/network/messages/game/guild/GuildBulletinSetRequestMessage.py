from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class GuildBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
    content:str
    notifyMembers:bool
    

    def init(self, content_:str, notifyMembers_:bool):
        self.content = content_
        self.notifyMembers = notifyMembers_
        
        super().__init__()
    
    
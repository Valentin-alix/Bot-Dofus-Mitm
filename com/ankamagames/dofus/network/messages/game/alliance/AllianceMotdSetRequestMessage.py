from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage


class AllianceMotdSetRequestMessage(SocialNoticeSetRequestMessage):
    content:str
    

    def init(self, content_:str):
        self.content = content_
        
        super().__init__()
    
    
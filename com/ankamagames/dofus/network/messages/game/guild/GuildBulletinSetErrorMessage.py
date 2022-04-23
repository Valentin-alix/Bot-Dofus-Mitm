from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetErrorMessage import SocialNoticeSetErrorMessage


class GuildBulletinSetErrorMessage(SocialNoticeSetErrorMessage):
    

    def init(self, reason_:int):
        
        super().__init__(reason_)
    
    
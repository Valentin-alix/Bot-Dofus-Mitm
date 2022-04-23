from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetErrorMessage import SocialNoticeSetErrorMessage


class AllianceMotdSetErrorMessage(SocialNoticeSetErrorMessage):
    

    def init(self, reason_:int):
        
        super().__init__(reason_)
    
    
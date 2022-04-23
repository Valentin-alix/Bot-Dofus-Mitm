from com.ankamagames.dofus.network.messages.game.social.SocialNoticeMessage import SocialNoticeMessage


class BulletinMessage(SocialNoticeMessage):
    lastNotifiedTimestamp:int
    

    def init(self, lastNotifiedTimestamp_:int, content_:str, timestamp_:int, memberId_:int, memberName_:str):
        self.lastNotifiedTimestamp = lastNotifiedTimestamp_
        
        super().__init__(content_, timestamp_, memberId_, memberName_)
    
    
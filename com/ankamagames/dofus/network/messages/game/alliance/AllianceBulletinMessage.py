from com.ankamagames.dofus.network.messages.game.social.BulletinMessage import BulletinMessage


class AllianceBulletinMessage(BulletinMessage):
    

    def init(self, lastNotifiedTimestamp_:int, content_:str, timestamp_:int, memberId_:int, memberName_:str):
        
        super().__init__(lastNotifiedTimestamp_, content_, timestamp_, memberId_, memberName_)
    
    
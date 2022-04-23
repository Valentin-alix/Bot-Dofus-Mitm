from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SocialNoticeMessage(NetworkMessage):
    content:str
    timestamp:int
    memberId:int
    memberName:str
    

    def init(self, content_:str, timestamp_:int, memberId_:int, memberName_:str):
        self.content = content_
        self.timestamp = timestamp_
        self.memberId = memberId_
        self.memberName = memberName_
        
        super().__init__()
    
    
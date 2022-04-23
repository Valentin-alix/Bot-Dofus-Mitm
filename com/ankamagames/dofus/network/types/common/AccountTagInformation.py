from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountTagInformation(NetworkMessage):
    nickname:str
    tagNumber:str
    

    def init(self, nickname_:str, tagNumber_:str):
        self.nickname = nickname_
        self.tagNumber = tagNumber_
        
        super().__init__()
    
    
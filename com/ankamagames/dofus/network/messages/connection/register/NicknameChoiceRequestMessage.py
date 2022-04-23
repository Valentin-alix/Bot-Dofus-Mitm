from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NicknameChoiceRequestMessage(NetworkMessage):
    nickname:str
    

    def init(self, nickname_:str):
        self.nickname = nickname_
        
        super().__init__()
    
    
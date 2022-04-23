from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MoodSmileyResultMessage(NetworkMessage):
    resultCode:int
    smileyId:int
    

    def init(self, resultCode_:int, smileyId_:int):
        self.resultCode = resultCode_
        self.smileyId = smileyId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCanBeCreatedResultMessage(NetworkMessage):
    yesYouCan:bool
    

    def init(self, yesYouCan_:bool):
        self.yesYouCan = yesYouCan_
        
        super().__init__()
    
    
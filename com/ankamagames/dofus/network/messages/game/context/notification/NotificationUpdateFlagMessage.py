from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NotificationUpdateFlagMessage(NetworkMessage):
    index:int
    

    def init(self, index_:int):
        self.index = index_
        
        super().__init__()
    
    
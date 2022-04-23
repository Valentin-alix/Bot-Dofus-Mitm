from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NotificationListMessage(NetworkMessage):
    flags:list[int]
    

    def init(self, flags_:list[int]):
        self.flags = flags_
        
        super().__init__()
    
    
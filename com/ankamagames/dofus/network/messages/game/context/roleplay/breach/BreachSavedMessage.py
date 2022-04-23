from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachSavedMessage(NetworkMessage):
    saved:bool
    

    def init(self, saved_:bool):
        self.saved = saved_
        
        super().__init__()
    
    
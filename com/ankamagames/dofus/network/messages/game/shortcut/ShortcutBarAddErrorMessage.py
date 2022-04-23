from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShortcutBarAddErrorMessage(NetworkMessage):
    error:int
    

    def init(self, error_:int):
        self.error = error_
        
        super().__init__()
    
    
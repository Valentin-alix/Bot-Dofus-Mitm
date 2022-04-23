from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameContextCreateMessage(NetworkMessage):
    context:int
    

    def init(self, context_:int):
        self.context = context_
        
        super().__init__()
    
    
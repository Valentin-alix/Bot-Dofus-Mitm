from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectEffect(NetworkMessage):
    actionId:int
    

    def init(self, actionId_:int):
        self.actionId = actionId_
        
        super().__init__()
    
    
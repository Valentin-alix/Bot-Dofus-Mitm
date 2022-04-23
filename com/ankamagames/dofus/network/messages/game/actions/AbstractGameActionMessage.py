from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractGameActionMessage(NetworkMessage):
    actionId:int
    sourceId:int
    

    def init(self, actionId_:int, sourceId_:int):
        self.actionId = actionId_
        self.sourceId = sourceId_
        
        super().__init__()
    
    
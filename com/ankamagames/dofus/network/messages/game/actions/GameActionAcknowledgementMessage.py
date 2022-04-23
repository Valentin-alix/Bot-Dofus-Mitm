from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionAcknowledgementMessage(NetworkMessage):
    valid:bool
    actionId:int
    

    def init(self, valid_:bool, actionId_:int):
        self.valid = valid_
        self.actionId = actionId_
        
        super().__init__()
    
    
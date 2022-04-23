from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StartupActionFinishedMessage(NetworkMessage):
    actionId:int
    success:bool
    automaticAction:bool
    success:bool
    automaticAction:bool
    

    def init(self, actionId_:int, success_:bool, automaticAction_:bool):
        self.actionId = actionId_
        self.success = success_
        self.automaticAction = automaticAction_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NotificationByServerMessage(NetworkMessage):
    id:int
    parameters:list[str]
    forceOpen:bool
    

    def init(self, id_:int, parameters_:list[str], forceOpen_:bool):
        self.id = id_
        self.parameters = parameters_
        self.forceOpen = forceOpen_
        
        super().__init__()
    
    
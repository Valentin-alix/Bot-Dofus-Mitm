from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiValidationMessage(NetworkMessage):
    action:int
    code:int
    

    def init(self, action_:int, code_:int):
        self.action = action_
        self.code = code_
        
        super().__init__()
    
    
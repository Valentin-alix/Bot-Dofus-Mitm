from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceCreationResultMessage(NetworkMessage):
    result:int
    

    def init(self, result_:int):
        self.result = result_
        
        super().__init__()
    
    
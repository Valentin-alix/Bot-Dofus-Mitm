from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountEquipedErrorMessage(NetworkMessage):
    errorType:int
    

    def init(self, errorType_:int):
        self.errorType = errorType_
        
        super().__init__()
    
    
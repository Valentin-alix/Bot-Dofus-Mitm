from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SlaveNoLongerControledMessage(NetworkMessage):
    masterId:int
    slaveId:int
    

    def init(self, masterId_:int, slaveId_:int):
        self.masterId = masterId_
        self.slaveId = slaveId_
        
        super().__init__()
    
    
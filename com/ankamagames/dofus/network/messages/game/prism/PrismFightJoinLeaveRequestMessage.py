from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightJoinLeaveRequestMessage(NetworkMessage):
    subAreaId:int
    join:bool
    

    def init(self, subAreaId_:int, join_:bool):
        self.subAreaId = subAreaId_
        self.join = join_
        
        super().__init__()
    
    
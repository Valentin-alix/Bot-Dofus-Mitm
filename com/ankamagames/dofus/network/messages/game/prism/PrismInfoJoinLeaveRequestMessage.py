from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismInfoJoinLeaveRequestMessage(NetworkMessage):
    join:bool
    

    def init(self, join_:bool):
        self.join = join_
        
        super().__init__()
    
    
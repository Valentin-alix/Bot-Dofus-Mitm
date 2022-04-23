from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebtsDeleteMessage(NetworkMessage):
    reason:int
    debts:list[int]
    

    def init(self, reason_:int, debts_:list[int]):
        self.reason = reason_
        self.debts = debts_
        
        super().__init__()
    
    
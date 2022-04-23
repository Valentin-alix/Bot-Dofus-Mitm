from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaginationAnswerAbstractMessage(NetworkMessage):
    offset:int
    count:int
    total:int
    

    def init(self, offset_:int, count_:int, total_:int):
        self.offset = offset_
        self.count = count_
        self.total = total_
        
        super().__init__()
    
    
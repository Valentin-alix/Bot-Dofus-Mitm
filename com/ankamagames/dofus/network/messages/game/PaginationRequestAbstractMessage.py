from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaginationRequestAbstractMessage(NetworkMessage):
    offset:int
    count:int
    

    def init(self, offset_:int, count_:int):
        self.offset = offset_
        self.count = count_
        
        super().__init__()
    
    
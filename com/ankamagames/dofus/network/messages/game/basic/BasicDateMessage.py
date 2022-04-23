from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicDateMessage(NetworkMessage):
    day:int
    month:int
    year:int
    

    def init(self, day_:int, month_:int, year_:int):
        self.day = day_
        self.month = month_
        self.year = year_
        
        super().__init__()
    
    
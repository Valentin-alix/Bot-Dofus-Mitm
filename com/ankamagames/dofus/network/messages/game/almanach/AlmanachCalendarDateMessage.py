from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlmanachCalendarDateMessage(NetworkMessage):
    date:int
    

    def init(self, date_:int):
        self.date = date_
        
        super().__init__()
    
    
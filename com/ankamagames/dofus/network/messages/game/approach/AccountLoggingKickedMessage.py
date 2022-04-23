from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountLoggingKickedMessage(NetworkMessage):
    days:int
    hours:int
    minutes:int
    

    def init(self, days_:int, hours_:int, minutes_:int):
        self.days = days_
        self.hours = hours_
        self.minutes = minutes_
        
        super().__init__()
    
    
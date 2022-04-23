from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountInformationsUpdateMessage(NetworkMessage):
    subscriptionEndDate:int
    

    def init(self, subscriptionEndDate_:int):
        self.subscriptionEndDate = subscriptionEndDate_
        
        super().__init__()
    
    
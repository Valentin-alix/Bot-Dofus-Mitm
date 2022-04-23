from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiConfirmationMessage(NetworkMessage):
    kamas:int
    amount:int
    rate:int
    action:int
    transaction:str
    

    def init(self, kamas_:int, amount_:int, rate_:int, action_:int, transaction_:str):
        self.kamas = kamas_
        self.amount = amount_
        self.rate = rate_
        self.action = action_
        self.transaction = transaction_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiConfirmationRequestMessage(NetworkMessage):
    kamas:int
    ogrines:int
    rate:int
    action:int
    

    def init(self, kamas_:int, ogrines_:int, rate_:int, action_:int):
        self.kamas = kamas_
        self.ogrines = ogrines_
        self.rate = rate_
        self.action = action_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeCrafterJobLevelupMessage(NetworkMessage):
    crafterJobLevel:int
    

    def init(self, crafterJobLevel_:int):
        self.crafterJobLevel = crafterJobLevel_
        
        super().__init__()
    
    
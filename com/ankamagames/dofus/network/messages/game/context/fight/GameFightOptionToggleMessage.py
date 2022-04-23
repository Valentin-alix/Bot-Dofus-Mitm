from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightOptionToggleMessage(NetworkMessage):
    option:int
    

    def init(self, option_:int):
        self.option = option_
        
        super().__init__()
    
    
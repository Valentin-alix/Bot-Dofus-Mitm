from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StatsUpgradeResultMessage(NetworkMessage):
    result:int
    nbCharacBoost:int
    

    def init(self, result_:int, nbCharacBoost_:int):
        self.result = result_
        self.nbCharacBoost = nbCharacBoost_
        
        super().__init__()
    
    
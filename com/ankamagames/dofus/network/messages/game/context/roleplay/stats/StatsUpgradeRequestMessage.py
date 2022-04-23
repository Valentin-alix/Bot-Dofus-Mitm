from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StatsUpgradeRequestMessage(NetworkMessage):
    useAdditionnal:bool
    statId:int
    boostPoint:int
    

    def init(self, useAdditionnal_:bool, statId_:int, boostPoint_:int):
        self.useAdditionnal = useAdditionnal_
        self.statId = statId_
        self.boostPoint = boostPoint_
        
        super().__init__()
    
    
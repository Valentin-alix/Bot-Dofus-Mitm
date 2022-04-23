from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntLegendaryRequestMessage(NetworkMessage):
    legendaryId:int
    

    def init(self, legendaryId_:int):
        self.legendaryId = legendaryId_
        
        super().__init__()
    
    
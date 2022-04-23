from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntShowLegendaryUIMessage(NetworkMessage):
    availableLegendaryIds:list[int]
    

    def init(self, availableLegendaryIds_:list[int]):
        self.availableLegendaryIds = availableLegendaryIds_
        
        super().__init__()
    
    
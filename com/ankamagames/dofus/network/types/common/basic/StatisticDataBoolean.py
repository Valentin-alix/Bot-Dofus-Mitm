from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


class StatisticDataBoolean(StatisticData):
    value:bool
    

    def init(self, value_:bool):
        self.value = value_
        
        super().__init__()
    
    
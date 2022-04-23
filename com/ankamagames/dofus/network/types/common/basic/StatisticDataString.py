from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


class StatisticDataString(StatisticData):
    value:str
    

    def init(self, value_:str):
        self.value = value_
        
        super().__init__()
    
    
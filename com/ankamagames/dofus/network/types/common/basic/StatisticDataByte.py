from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


class StatisticDataByte(StatisticData):
    value:int
    

    def init(self, value_:int):
        self.value = value_
        
        super().__init__()
    
    
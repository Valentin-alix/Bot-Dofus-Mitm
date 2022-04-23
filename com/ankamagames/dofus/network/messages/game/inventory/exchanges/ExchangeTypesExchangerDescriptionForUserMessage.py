from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeTypesExchangerDescriptionForUserMessage(NetworkMessage):
    objectType:int
    typeDescription:list[int]
    

    def init(self, objectType_:int, typeDescription_:list[int]):
        self.objectType = objectType_
        self.typeDescription = typeDescription_
        
        super().__init__()
    
    
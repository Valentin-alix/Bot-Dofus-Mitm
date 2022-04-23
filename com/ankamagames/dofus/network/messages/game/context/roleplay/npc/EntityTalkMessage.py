from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityTalkMessage(NetworkMessage):
    entityId:int
    textId:int
    parameters:list[str]
    

    def init(self, entityId_:int, textId_:int, parameters_:list[str]):
        self.entityId = entityId_
        self.textId = textId_
        self.parameters = parameters_
        
        super().__init__()
    
    
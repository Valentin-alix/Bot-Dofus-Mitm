from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameContextRemoveMultipleElementsMessage(NetworkMessage):
    elementsIds:list[int]
    

    def init(self, elementsIds_:list[int]):
        self.elementsIds = elementsIds_
        
        super().__init__()
    
    
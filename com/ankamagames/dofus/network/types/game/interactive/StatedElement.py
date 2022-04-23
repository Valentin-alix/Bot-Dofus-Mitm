from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StatedElement(NetworkMessage):
    elementId:int
    elementCellId:int
    elementState:int
    onCurrentMap:bool
    

    def init(self, elementId_:int, elementCellId_:int, elementState_:int, onCurrentMap_:bool):
        self.elementId = elementId_
        self.elementCellId = elementCellId_
        self.elementState = elementState_
        self.onCurrentMap = onCurrentMap_
        
        super().__init__()
    
    
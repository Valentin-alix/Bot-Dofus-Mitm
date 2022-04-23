from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveElementMessage import GameContextRemoveElementMessage


class GameContextRemoveElementWithEventMessage(GameContextRemoveElementMessage):
    elementEventId:int
    

    def init(self, elementEventId_:int, id_:int):
        self.elementEventId = elementEventId_
        
        super().__init__(id_)
    
    
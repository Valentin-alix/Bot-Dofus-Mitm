from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveMultipleElementsMessage import GameContextRemoveMultipleElementsMessage


class GameContextRemoveMultipleElementsWithEventsMessage(GameContextRemoveMultipleElementsMessage):
    elementEventIds:list[int]
    

    def init(self, elementEventIds_:list[int], elementsIds_:list[int]):
        self.elementEventIds = elementEventIds_
        
        super().__init__(elementsIds_)
    
    
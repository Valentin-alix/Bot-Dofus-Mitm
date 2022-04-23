from com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage


class GuildListApplicationRequestMessage(PaginationRequestAbstractMessage):
    

    def init(self, offset_:int, count_:int):
        
        super().__init__(offset_, count_)
    
    
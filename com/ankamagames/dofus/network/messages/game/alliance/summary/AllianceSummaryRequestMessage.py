from com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage


class AllianceSummaryRequestMessage(PaginationRequestAbstractMessage):
    nameFilter:str
    tagFilter:str
    playerNameFilter:str
    sortType:int
    sortDescending:bool
    

    def init(self, nameFilter_:str, tagFilter_:str, playerNameFilter_:str, sortType_:int, sortDescending_:bool, offset_:int, count_:int):
        self.nameFilter = nameFilter_
        self.tagFilter = tagFilter_
        self.playerNameFilter = playerNameFilter_
        self.sortType = sortType_
        self.sortDescending = sortDescending_
        
        super().__init__(offset_, count_)
    
    
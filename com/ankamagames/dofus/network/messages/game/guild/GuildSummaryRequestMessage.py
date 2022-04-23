from com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage


class GuildSummaryRequestMessage(PaginationRequestAbstractMessage):
    nameFilter:str
    criterionFilter:list[int]
    languagesFilter:list[int]
    recruitmentTypeFilter:list[int]
    minLevelFilter:int
    maxLevelFilter:int
    minPlayerLevelFilter:int
    maxPlayerLevelFilter:int
    minSuccessFilter:int
    maxSuccessFilter:int
    sortType:int
    hideFullFilter:bool
    sortDescending:bool
    hideFullFilter:bool
    sortDescending:bool
    

    def init(self, nameFilter_:str, criterionFilter_:list[int], languagesFilter_:list[int], recruitmentTypeFilter_:list[int], minLevelFilter_:int, maxLevelFilter_:int, minPlayerLevelFilter_:int, maxPlayerLevelFilter_:int, minSuccessFilter_:int, maxSuccessFilter_:int, sortType_:int, hideFullFilter_:bool, sortDescending_:bool, offset_:int, count_:int):
        self.nameFilter = nameFilter_
        self.criterionFilter = criterionFilter_
        self.languagesFilter = languagesFilter_
        self.recruitmentTypeFilter = recruitmentTypeFilter_
        self.minLevelFilter = minLevelFilter_
        self.maxLevelFilter = maxLevelFilter_
        self.minPlayerLevelFilter = minPlayerLevelFilter_
        self.maxPlayerLevelFilter = maxPlayerLevelFilter_
        self.minSuccessFilter = minSuccessFilter_
        self.maxSuccessFilter = maxSuccessFilter_
        self.sortType = sortType_
        self.hideFullFilter = hideFullFilter_
        self.sortDescending = sortDescending_
        
        super().__init__(offset_, count_)
    
    
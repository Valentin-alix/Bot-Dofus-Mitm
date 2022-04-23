from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockInformationsForSell import PaddockInformationsForSell
    


class PaddockToSellListMessage(NetworkMessage):
    pageIndex:int
    totalPage:int
    paddockList:list['PaddockInformationsForSell']
    

    def init(self, pageIndex_:int, totalPage_:int, paddockList_:list['PaddockInformationsForSell']):
        self.pageIndex = pageIndex_
        self.totalPage = totalPage_
        self.paddockList = paddockList_
        
        super().__init__()
    
    
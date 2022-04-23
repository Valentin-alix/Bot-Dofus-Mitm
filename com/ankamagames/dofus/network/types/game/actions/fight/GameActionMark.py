from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMarkedCell import GameActionMarkedCell
    


class GameActionMark(NetworkMessage):
    markAuthorId:int
    markTeamId:int
    markSpellId:int
    markSpellLevel:int
    markId:int
    markType:int
    markimpactCell:int
    cells:list['GameActionMarkedCell']
    active:bool
    

    def init(self, markAuthorId_:int, markTeamId_:int, markSpellId_:int, markSpellLevel_:int, markId_:int, markType_:int, markimpactCell_:int, cells_:list['GameActionMarkedCell'], active_:bool):
        self.markAuthorId = markAuthorId_
        self.markTeamId = markTeamId_
        self.markSpellId = markSpellId_
        self.markSpellLevel = markSpellLevel_
        self.markId = markId_
        self.markType = markType_
        self.markimpactCell = markimpactCell_
        self.cells = cells_
        self.active = active_
        
        super().__init__()
    
    
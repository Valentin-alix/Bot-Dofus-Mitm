from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation
    


class DebtsUpdateMessage(NetworkMessage):
    action:int
    debts:list['DebtInformation']
    

    def init(self, action_:int, debts_:list['DebtInformation']):
        self.action = action_
        self.debts = debts_
        
        super().__init__()
    
    
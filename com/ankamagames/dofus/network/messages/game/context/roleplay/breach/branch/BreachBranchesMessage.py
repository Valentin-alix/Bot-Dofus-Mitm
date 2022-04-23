from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch
    


class BreachBranchesMessage(NetworkMessage):
    branches:list['ExtendedBreachBranch']
    

    def init(self, branches_:list['ExtendedBreachBranch']):
        self.branches = branches_
        
        super().__init__()
    
    
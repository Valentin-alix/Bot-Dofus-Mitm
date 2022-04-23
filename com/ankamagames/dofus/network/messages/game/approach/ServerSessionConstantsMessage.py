from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant
    


class ServerSessionConstantsMessage(NetworkMessage):
    variables:list['ServerSessionConstant']
    

    def init(self, variables_:list['ServerSessionConstant']):
        self.variables = variables_
        
        super().__init__()
    
    
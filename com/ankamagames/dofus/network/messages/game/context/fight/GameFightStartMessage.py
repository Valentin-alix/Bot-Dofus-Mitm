from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    


class GameFightStartMessage(NetworkMessage):
    idols:list['Idol']
    

    def init(self, idols_:list['Idol']):
        self.idols = idols_
        
        super().__init__()
    
    
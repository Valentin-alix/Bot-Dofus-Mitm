from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    


class IdolFightPreparationUpdateMessage(NetworkMessage):
    idolSource:int
    idols:list['Idol']
    

    def init(self, idolSource_:int, idols_:list['Idol']):
        self.idolSource = idolSource_
        self.idols = idols_
        
        super().__init__()
    
    
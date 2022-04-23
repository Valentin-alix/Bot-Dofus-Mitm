from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions
    


class MapFightStartPositionsUpdateMessage(NetworkMessage):
    mapId:int
    fightStartPositions:'FightStartingPositions'
    

    def init(self, mapId_:int, fightStartPositions_:'FightStartingPositions'):
        self.mapId = mapId_
        self.fightStartPositions = fightStartPositions_
        
        super().__init__()
    
    
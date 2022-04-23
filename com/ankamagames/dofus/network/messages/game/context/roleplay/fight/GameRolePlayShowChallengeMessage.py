from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations
    


class GameRolePlayShowChallengeMessage(NetworkMessage):
    commonsInfos:'FightCommonInformations'
    

    def init(self, commonsInfos_:'FightCommonInformations'):
        self.commonsInfos = commonsInfos_
        
        super().__init__()
    
    
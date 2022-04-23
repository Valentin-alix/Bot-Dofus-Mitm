from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward
    


class BreachRewardsMessage(NetworkMessage):
    rewards:list['BreachReward']
    

    def init(self, rewards_:list['BreachReward']):
        self.rewards = rewards_
        
        super().__init__()
    
    
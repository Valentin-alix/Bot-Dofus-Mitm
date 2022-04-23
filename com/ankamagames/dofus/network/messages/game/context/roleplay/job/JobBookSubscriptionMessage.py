from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobBookSubscription import JobBookSubscription
    


class JobBookSubscriptionMessage(NetworkMessage):
    subscriptions:list['JobBookSubscription']
    

    def init(self, subscriptions_:list['JobBookSubscription']):
        self.subscriptions = subscriptions_
        
        super().__init__()
    
    
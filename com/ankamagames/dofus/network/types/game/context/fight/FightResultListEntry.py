from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultListEntry(NetworkMessage):
    outcome:int
    wave:int
    rewards:'FightLoot'
    

    def init(self, outcome_:int, wave_:int, rewards_:'FightLoot'):
        self.outcome = outcome_
        self.wave = wave_
        self.rewards = rewards_
        
        super().__init__()
    
    
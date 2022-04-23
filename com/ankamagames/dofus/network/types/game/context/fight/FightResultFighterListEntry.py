from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultFighterListEntry(FightResultListEntry):
    id:int
    alive:bool
    

    def init(self, id_:int, alive_:bool, outcome_:int, wave_:int, rewards_:'FightLoot'):
        self.id = id_
        self.alive = alive_
        
        super().__init__(outcome_, wave_, rewards_)
    
    
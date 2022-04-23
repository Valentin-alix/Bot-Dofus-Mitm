from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultPlayerListEntry(FightResultFighterListEntry):
    level:int
    additional:list['FightResultAdditionalData']
    

    def init(self, level_:int, additional_:list['FightResultAdditionalData'], id_:int, alive_:bool, outcome_:int, wave_:int, rewards_:'FightLoot'):
        self.level = level_
        self.additional = additional_
        
        super().__init__(id_, alive_, outcome_, wave_, rewards_)
    
    
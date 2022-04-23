from com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    


class ExtendedLockedBreachBranch(ExtendedBreachBranch):
    unlockPrice:int
    

    def init(self, unlockPrice_:int, rewards_:list['BreachReward'], modifier_:int, prize_:int, room_:int, element_:int, bosses_:list['MonsterInGroupLightInformations'], map_:int, score_:int, relativeScore_:int, monsters_:list['MonsterInGroupLightInformations']):
        self.unlockPrice = unlockPrice_
        
        super().__init__(rewards_, modifier_, prize_, room_, element_, bosses_, map_, score_, relativeScore_, monsters_)
    
    
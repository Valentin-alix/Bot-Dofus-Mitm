from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    


class ExtendedBreachBranch(BreachBranch):
    rewards:list['BreachReward']
    modifier:int
    prize:int
    

    def init(self, rewards_:list['BreachReward'], modifier_:int, prize_:int, room_:int, element_:int, bosses_:list['MonsterInGroupLightInformations'], map_:int, score_:int, relativeScore_:int, monsters_:list['MonsterInGroupLightInformations']):
        self.rewards = rewards_
        self.modifier = modifier_
        self.prize = prize_
        
        super().__init__(room_, element_, bosses_, map_, score_, relativeScore_, monsters_)
    
    
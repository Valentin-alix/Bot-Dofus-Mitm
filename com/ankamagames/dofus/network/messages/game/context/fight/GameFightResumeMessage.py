from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSpectateMessage import GameFightSpectateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown
    from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
    


class GameFightResumeMessage(GameFightSpectateMessage):
    spellCooldowns:list['GameFightSpellCooldown']
    summonCount:int
    bombCount:int
    

    def init(self, spellCooldowns_:list['GameFightSpellCooldown'], summonCount_:int, bombCount_:int, effects_:list['FightDispellableEffectExtendedInformations'], marks_:list['GameActionMark'], gameTurn_:int, fightStart_:int, idols_:list['Idol'], fxTriggerCounts_:list['GameFightEffectTriggerCount']):
        self.spellCooldowns = spellCooldowns_
        self.summonCount = summonCount_
        self.bombCount = bombCount_
        
        super().__init__(effects_, marks_, gameTurn_, fightStart_, idols_, fxTriggerCounts_)
    
    
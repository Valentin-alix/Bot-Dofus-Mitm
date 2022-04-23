from com.ankamagames.dofus.network.messages.game.context.fight.GameFightResumeMessage import GameFightResumeMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown
    from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
    


class GameFightResumeWithSlavesMessage(GameFightResumeMessage):
    slavesInfo:list['GameFightResumeSlaveInfo']
    

    def init(self, slavesInfo_:list['GameFightResumeSlaveInfo'], spellCooldowns_:list['GameFightSpellCooldown'], summonCount_:int, bombCount_:int, effects_:list['FightDispellableEffectExtendedInformations'], marks_:list['GameActionMark'], gameTurn_:int, fightStart_:int, idols_:list['Idol'], fxTriggerCounts_:list['GameFightEffectTriggerCount']):
        self.slavesInfo = slavesInfo_
        
        super().__init__(spellCooldowns_, summonCount_, bombCount_, effects_, marks_, gameTurn_, fightStart_, idols_, fxTriggerCounts_)
    
    
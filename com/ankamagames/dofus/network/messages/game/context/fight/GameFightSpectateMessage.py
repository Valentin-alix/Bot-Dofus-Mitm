from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
    from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
    


class GameFightSpectateMessage(NetworkMessage):
    effects:list['FightDispellableEffectExtendedInformations']
    marks:list['GameActionMark']
    gameTurn:int
    fightStart:int
    idols:list['Idol']
    fxTriggerCounts:list['GameFightEffectTriggerCount']
    

    def init(self, effects_:list['FightDispellableEffectExtendedInformations'], marks_:list['GameActionMark'], gameTurn_:int, fightStart_:int, idols_:list['Idol'], fxTriggerCounts_:list['GameFightEffectTriggerCount']):
        self.effects = effects_
        self.marks = marks_
        self.gameTurn = gameTurn_
        self.fightStart = fightStart_
        self.idols = idols_
        self.fxTriggerCounts = fxTriggerCounts_
        
        super().__init__()
    
    
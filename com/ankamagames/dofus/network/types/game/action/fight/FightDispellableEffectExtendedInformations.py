from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect
    


class FightDispellableEffectExtendedInformations(NetworkMessage):
    actionId:int
    sourceId:int
    effect:'AbstractFightDispellableEffect'
    

    def init(self, actionId_:int, sourceId_:int, effect_:'AbstractFightDispellableEffect'):
        self.actionId = actionId_
        self.sourceId = sourceId_
        self.effect = effect_
        
        super().__init__()
    
    
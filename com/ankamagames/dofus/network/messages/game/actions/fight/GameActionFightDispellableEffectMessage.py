from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect
    


class GameActionFightDispellableEffectMessage(AbstractGameActionMessage):
    effect:'AbstractFightDispellableEffect'
    

    def init(self, effect_:'AbstractFightDispellableEffect', actionId_:int, sourceId_:int):
        self.effect = effect_
        
        super().__init__(actionId_, sourceId_)
    
    
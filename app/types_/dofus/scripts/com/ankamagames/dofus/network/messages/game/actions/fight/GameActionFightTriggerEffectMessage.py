from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellEffectMessage import GameActionFightDispellEffectMessage
if TYPE_CHECKING:
	...
class GameActionFightTriggerEffectMessage(GameActionFightDispellEffectMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...
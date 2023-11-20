from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import GameFightEndMessage
if TYPE_CHECKING:
	...
class BreachGameFightEndMessage(GameFightEndMessage):
	def __init__(self, budget:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.budget=budget
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.GameContextRemoveMultipleElementsMessage import GameContextRemoveMultipleElementsMessage
if TYPE_CHECKING:
	...
class GameContextRemoveMultipleElementsWithEventsMessage(GameContextRemoveMultipleElementsMessage):
	def __init__(self, elementEventIds:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.elementEventIds=elementEventIds
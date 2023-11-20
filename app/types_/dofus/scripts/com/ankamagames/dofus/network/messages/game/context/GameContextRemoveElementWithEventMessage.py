from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.GameContextRemoveElementMessage import GameContextRemoveElementMessage
if TYPE_CHECKING:
	...
class GameContextRemoveElementWithEventMessage(GameContextRemoveElementMessage):
	def __init__(self, elementEventId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.elementEventId=elementEventId
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntDigRequestAnswerMessage import TreasureHuntDigRequestAnswerMessage
if TYPE_CHECKING:
	...
class TreasureHuntDigRequestAnswerFailedMessage(TreasureHuntDigRequestAnswerMessage):
	def __init__(self, wrongFlagCount:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.wrongFlagCount=wrongFlagCount
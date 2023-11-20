from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.GameMapMovementRequestMessage import GameMapMovementRequestMessage
if TYPE_CHECKING:
	...
class GameCautiousMapMovementRequestMessage(GameMapMovementRequestMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...
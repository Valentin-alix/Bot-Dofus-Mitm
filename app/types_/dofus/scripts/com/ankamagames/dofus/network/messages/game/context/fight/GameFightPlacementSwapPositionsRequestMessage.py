from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementPositionRequestMessage import GameFightPlacementPositionRequestMessage
if TYPE_CHECKING:
	...
class GameFightPlacementSwapPositionsRequestMessage(GameFightPlacementPositionRequestMessage):
	def __init__(self, requestedId:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.requestedId=requestedId
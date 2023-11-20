from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightSpectatePlayerRequestMessage:
	def __init__(self, playerId:int):
		self.playerId=playerId
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChallengeFightJoinRefusedMessage:
	def __init__(self, playerId:int, reason:int):
		self.playerId=playerId
		self.reason=reason
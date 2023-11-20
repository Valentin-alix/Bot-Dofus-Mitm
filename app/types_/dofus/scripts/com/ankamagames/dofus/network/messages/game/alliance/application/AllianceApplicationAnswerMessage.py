from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceApplicationAnswerMessage:
	def __init__(self, accepted:bool, playerId:int):
		self.accepted=accepted
		self.playerId=playerId
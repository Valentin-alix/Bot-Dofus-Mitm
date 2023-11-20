from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightNewRoundMessage:
	def __init__(self, roundNumber:int):
		self.roundNumber=roundNumber
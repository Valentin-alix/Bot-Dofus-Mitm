from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightJoinMessage:
	def __init__(self, timeMaxBeforeFightStart:int, fightType:int):
		self.timeMaxBeforeFightStart=timeMaxBeforeFightStart
		self.fightType=fightType
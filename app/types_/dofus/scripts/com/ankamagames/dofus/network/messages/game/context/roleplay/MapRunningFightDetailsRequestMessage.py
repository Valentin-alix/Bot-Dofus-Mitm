from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MapRunningFightDetailsRequestMessage:
	def __init__(self, fightId:int):
		self.fightId=fightId
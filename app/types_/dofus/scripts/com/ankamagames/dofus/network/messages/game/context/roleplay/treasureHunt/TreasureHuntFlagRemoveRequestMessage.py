from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TreasureHuntFlagRemoveRequestMessage:
	def __init__(self, questType:int, index:int):
		self.questType=questType
		self.index=index
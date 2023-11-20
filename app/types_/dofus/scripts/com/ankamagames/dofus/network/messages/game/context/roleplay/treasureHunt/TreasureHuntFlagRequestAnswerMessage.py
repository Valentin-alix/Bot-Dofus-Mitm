from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TreasureHuntFlagRequestAnswerMessage:
	def __init__(self, questType:int, result:int, index:int):
		self.questType=questType
		self.result=result
		self.index=index
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TreasureHuntDigRequestAnswerMessage:
	def __init__(self, questType:int, result:int):
		self.questType=questType
		self.result=result
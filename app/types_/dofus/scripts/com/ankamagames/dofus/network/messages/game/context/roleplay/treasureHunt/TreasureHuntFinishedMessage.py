from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TreasureHuntFinishedMessage:
	def __init__(self, questType:int):
		self.questType=questType
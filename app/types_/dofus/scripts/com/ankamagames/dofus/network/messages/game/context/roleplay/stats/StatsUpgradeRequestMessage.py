from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class StatsUpgradeRequestMessage:
	def __init__(self, useAdditionnal:bool, statId:int, boostPoint:int):
		self.useAdditionnal=useAdditionnal
		self.statId=statId
		self.boostPoint=boostPoint
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class StatsUpgradeResultMessage:
	def __init__(self, result:int, nbCharacBoost:int):
		self.result=result
		self.nbCharacBoost=nbCharacBoost
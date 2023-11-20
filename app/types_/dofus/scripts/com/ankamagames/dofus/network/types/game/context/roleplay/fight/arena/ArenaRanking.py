from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ArenaRanking:
	def __init__(self, rank:int, bestRank:int):
		self.rank=rank
		self.bestRank=bestRank
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AlignmentRankUpdateMessage:
	def __init__(self, alignmentRank:int, verbose:bool):
		self.alignmentRank=alignmentRank
		self.verbose=verbose
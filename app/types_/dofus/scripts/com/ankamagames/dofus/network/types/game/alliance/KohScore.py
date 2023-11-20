from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class KohScore:
	def __init__(self, avaScoreTypeEnum:int, roundScores:int, cumulScores:int):
		self.avaScoreTypeEnum=avaScoreTypeEnum
		self.roundScores=roundScores
		self.cumulScores=cumulScores
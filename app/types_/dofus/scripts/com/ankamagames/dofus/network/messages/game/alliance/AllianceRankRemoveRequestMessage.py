from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceRankRemoveRequestMessage:
	def __init__(self, rankId:int, newRankId:int):
		self.rankId=rankId
		self.newRankId=newRankId
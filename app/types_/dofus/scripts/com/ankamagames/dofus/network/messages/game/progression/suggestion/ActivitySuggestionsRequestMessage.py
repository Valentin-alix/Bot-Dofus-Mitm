from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ActivitySuggestionsRequestMessage:
	def __init__(self, minLevel:int, maxLevel:int, areaId:int, activityCategoryId:int, nbCards:int):
		self.minLevel=minLevel
		self.maxLevel=maxLevel
		self.areaId=areaId
		self.activityCategoryId=activityCategoryId
		self.nbCards=nbCards
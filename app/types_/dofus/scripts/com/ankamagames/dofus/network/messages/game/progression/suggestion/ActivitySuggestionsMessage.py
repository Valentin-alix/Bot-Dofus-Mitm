from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ActivitySuggestionsMessage:
	def __init__(self, lockedActivitiesIds:list[int], unlockedActivitiesIds:list[int]):
		self.lockedActivitiesIds=lockedActivitiesIds
		self.unlockedActivitiesIds=unlockedActivitiesIds
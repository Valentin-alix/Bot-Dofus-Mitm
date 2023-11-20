from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AchievementObjective:
	def __init__(self, id:int, maxValue:int):
		self.id=id
		self.maxValue=maxValue
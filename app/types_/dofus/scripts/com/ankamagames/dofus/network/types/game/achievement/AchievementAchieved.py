from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AchievementAchieved:
	def __init__(self, id:int, achievedBy:int):
		self.id=id
		self.achievedBy=achievedBy
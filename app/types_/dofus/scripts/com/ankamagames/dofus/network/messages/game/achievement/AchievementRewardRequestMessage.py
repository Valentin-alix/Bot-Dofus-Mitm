from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AchievementRewardRequestMessage:
	def __init__(self, achievementId:int):
		self.achievementId=achievementId
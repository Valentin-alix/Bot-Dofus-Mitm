from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.achievement.AchievementAchievedRewardable import AchievementAchievedRewardable
class AchievementFinishedMessage:
	def __init__(self, achievement:AchievementAchievedRewardable):
		self.achievement=achievement
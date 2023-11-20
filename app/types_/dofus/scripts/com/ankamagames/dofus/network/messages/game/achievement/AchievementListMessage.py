from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved
class AchievementListMessage:
	def __init__(self, finishedAchievements:list[AchievementAchieved]):
		self.finishedAchievements=finishedAchievements
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
class AchievementDetailedListMessage:
	def __init__(self, startedAchievements:list[Achievement], finishedAchievements:list[Achievement]):
		self.startedAchievements=startedAchievements
		self.finishedAchievements=finishedAchievements
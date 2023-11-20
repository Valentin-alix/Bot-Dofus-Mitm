from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
class AchievementAlmostFinishedDetailedListMessage:
	def __init__(self, almostFinishedAchievements:list[Achievement]):
		self.almostFinishedAchievements=almostFinishedAchievements
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved
if TYPE_CHECKING:
	...
class AchievementAchievedRewardable(AchievementAchieved):
	def __init__(self, finishedlevel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.finishedlevel=finishedlevel
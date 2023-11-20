from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.achievement.AchievementStartedObjective import AchievementStartedObjective
class Achievement:
	def __init__(self, id:int, finishedObjective:list[AchievementObjective], startedObjectives:list[AchievementStartedObjective]):
		self.id=id
		self.finishedObjective=finishedObjective
		self.startedObjectives=startedObjectives
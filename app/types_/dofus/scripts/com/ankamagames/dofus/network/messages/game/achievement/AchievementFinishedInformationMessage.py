from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.achievement.AchievementFinishedMessage import AchievementFinishedMessage
if TYPE_CHECKING:
	...
class AchievementFinishedInformationMessage(AchievementFinishedMessage):
	def __init__(self, name:str, playerId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name=name
		self.playerId=playerId
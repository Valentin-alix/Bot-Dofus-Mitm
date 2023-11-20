from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobAllowMultiCraftRequestMessage import JobAllowMultiCraftRequestMessage
if TYPE_CHECKING:
	...
class JobMultiCraftAvailableSkillsMessage(JobAllowMultiCraftRequestMessage):
	def __init__(self, playerId:int, skills:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId
		self.skills=skills
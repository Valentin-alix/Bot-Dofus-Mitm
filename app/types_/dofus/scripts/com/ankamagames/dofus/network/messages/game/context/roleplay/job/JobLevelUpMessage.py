from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import JobDescription
class JobLevelUpMessage:
	def __init__(self, newLevel:int, jobsDescription:JobDescription):
		self.newLevel=newLevel
		self.jobsDescription=jobsDescription
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobExperience import JobExperience
class JobExperienceMultiUpdateMessage:
	def __init__(self, experiencesUpdate:list[JobExperience]):
		self.experiencesUpdate=experiencesUpdate
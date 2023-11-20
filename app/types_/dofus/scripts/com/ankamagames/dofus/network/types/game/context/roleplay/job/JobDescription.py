from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription
class JobDescription:
	def __init__(self, jobId:int, skills:list[SkillActionDescription]):
		self.jobId=jobId
		self.skills=skills
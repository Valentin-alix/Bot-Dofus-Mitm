from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription
if TYPE_CHECKING:
	...
class SkillActionDescriptionTimed(SkillActionDescription):
	def __init__(self, time:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.time=time
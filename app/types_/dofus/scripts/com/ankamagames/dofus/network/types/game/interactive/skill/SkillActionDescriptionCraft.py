from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription
if TYPE_CHECKING:
	...
class SkillActionDescriptionCraft(SkillActionDescription):
	def __init__(self, probability:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.probability=probability
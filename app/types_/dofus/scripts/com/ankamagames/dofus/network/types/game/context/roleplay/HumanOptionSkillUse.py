from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
if TYPE_CHECKING:
	...
class HumanOptionSkillUse(HumanOption):
	def __init__(self, elementId:int, skillId:int, skillEndTime:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.elementId=elementId
		self.skillId=skillId
		self.skillEndTime=skillEndTime
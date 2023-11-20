from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
class InteractiveElement:
	def __init__(self, elementId:int, elementTypeId:int, enabledSkills:list[InteractiveElementSkill], disabledSkills:list[InteractiveElementSkill], onCurrentMap:bool):
		self.elementId=elementId
		self.elementTypeId=elementTypeId
		self.enabledSkills=enabledSkills
		self.disabledSkills=disabledSkills
		self.onCurrentMap=onCurrentMap
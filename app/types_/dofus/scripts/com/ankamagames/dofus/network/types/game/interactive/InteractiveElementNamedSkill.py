from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
if TYPE_CHECKING:
	...
class InteractiveElementNamedSkill(InteractiveElementSkill):
	def __init__(self, nameId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.nameId=nameId
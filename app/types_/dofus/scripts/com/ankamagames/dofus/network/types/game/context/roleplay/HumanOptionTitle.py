from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
if TYPE_CHECKING:
	...
class HumanOptionTitle(HumanOption):
	def __init__(self, titleId:int, titleParam:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.titleId=titleId
		self.titleParam=titleParam
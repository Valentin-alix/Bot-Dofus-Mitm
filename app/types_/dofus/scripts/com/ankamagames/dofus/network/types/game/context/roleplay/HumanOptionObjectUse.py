from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
if TYPE_CHECKING:
	...
class HumanOptionObjectUse(HumanOption):
	def __init__(self, delayTypeId:int, delayEndTime:float, objectGID:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.delayTypeId=delayTypeId
		self.delayEndTime=delayEndTime
		self.objectGID=objectGID
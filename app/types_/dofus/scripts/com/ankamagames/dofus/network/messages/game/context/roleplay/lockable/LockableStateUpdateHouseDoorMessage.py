from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage
if TYPE_CHECKING:
	...
class LockableStateUpdateHouseDoorMessage(LockableStateUpdateAbstractMessage):
	def __init__(self, houseId:int, instanceId:int, secondHand:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.houseId=houseId
		self.instanceId=instanceId
		self.secondHand=secondHand
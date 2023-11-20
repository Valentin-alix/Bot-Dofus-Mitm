from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage
if TYPE_CHECKING:
	...
class LockableStateUpdateStorageMessage(LockableStateUpdateAbstractMessage):
	def __init__(self, mapId:float, elementId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.mapId=mapId
		self.elementId=elementId
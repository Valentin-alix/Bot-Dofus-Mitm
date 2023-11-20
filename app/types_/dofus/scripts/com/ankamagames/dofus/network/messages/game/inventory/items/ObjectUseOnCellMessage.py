from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage
if TYPE_CHECKING:
	...
class ObjectUseOnCellMessage(ObjectUseMessage):
	def __init__(self, cells:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.cells=cells
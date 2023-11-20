from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectErrorMessage import ObjectErrorMessage
if TYPE_CHECKING:
	...
class SymbioticObjectErrorMessage(ObjectErrorMessage):
	def __init__(self, errorCode:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.errorCode=errorCode
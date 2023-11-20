from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectErrorMessage import SymbioticObjectErrorMessage
if TYPE_CHECKING:
	...
class MimicryObjectErrorMessage(SymbioticObjectErrorMessage):
	def __init__(self, preview:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.preview=preview
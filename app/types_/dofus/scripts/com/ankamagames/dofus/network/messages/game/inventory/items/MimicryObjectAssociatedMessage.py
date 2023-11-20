from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociatedMessage import SymbioticObjectAssociatedMessage
if TYPE_CHECKING:
	...
class MimicryObjectAssociatedMessage(SymbioticObjectAssociatedMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...
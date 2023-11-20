from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociateRequestMessage import SymbioticObjectAssociateRequestMessage
if TYPE_CHECKING:
	...
class MimicryObjectFeedAndAssociateRequestMessage(SymbioticObjectAssociateRequestMessage):
	def __init__(self, foodUID:int, foodPos:int, preview:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.foodUID=foodUID
		self.foodPos=foodPos
		self.preview=preview
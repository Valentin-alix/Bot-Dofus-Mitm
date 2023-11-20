from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.inventory.exchanges.RecycledItem import RecycledItem
class EvolutiveObjectRecycleResultMessage:
	def __init__(self, recycledItems:list[RecycledItem]):
		self.recycledItems=recycledItems
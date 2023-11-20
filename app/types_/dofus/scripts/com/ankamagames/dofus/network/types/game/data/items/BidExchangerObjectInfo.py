from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
class BidExchangerObjectInfo:
	def __init__(self, objectUID:int, objectGID:int, objectType:int, effects:list[ObjectEffect], prices:list[int]):
		self.objectUID=objectUID
		self.objectGID=objectGID
		self.objectType=objectType
		self.effects=effects
		self.prices=prices
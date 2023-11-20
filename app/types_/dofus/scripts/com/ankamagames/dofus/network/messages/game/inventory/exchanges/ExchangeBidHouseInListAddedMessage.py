from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
class ExchangeBidHouseInListAddedMessage:
	def __init__(self, itemUID:int, objectGID:int, objectType:int, effects:list[ObjectEffect], prices:list[int]):
		self.itemUID=itemUID
		self.objectGID=objectGID
		self.objectType=objectType
		self.effects=effects
		self.prices=prices
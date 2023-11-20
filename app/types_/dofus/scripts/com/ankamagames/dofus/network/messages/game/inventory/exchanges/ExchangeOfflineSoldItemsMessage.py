from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
class ExchangeOfflineSoldItemsMessage:
	def __init__(self, bidHouseItems:list[ObjectItemQuantityPriceDateEffects]):
		self.bidHouseItems=bidHouseItems
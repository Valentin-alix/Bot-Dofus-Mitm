from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop
class ExchangeStartOkNpcShopMessage:
	def __init__(self, npcSellerId:float, tokenId:int, objectsInfos:list[ObjectItemToSellInNpcShop]):
		self.npcSellerId=npcSellerId
		self.tokenId=tokenId
		self.objectsInfos=objectsInfos
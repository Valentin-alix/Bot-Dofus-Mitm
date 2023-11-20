from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInformationsForSell import HouseInformationsForSell
class HouseToSellListMessage:
	def __init__(self, pageIndex:int, totalPage:int, houseList:list[HouseInformationsForSell]):
		self.pageIndex=pageIndex
		self.totalPage=totalPage
		self.houseList=houseList
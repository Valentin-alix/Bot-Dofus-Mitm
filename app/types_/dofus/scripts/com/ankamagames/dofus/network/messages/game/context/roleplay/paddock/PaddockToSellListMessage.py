from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.PaddockInformationsForSell import PaddockInformationsForSell
class PaddockToSellListMessage:
	def __init__(self, pageIndex:int, totalPage:int, paddockList:list[PaddockInformationsForSell]):
		self.pageIndex=pageIndex
		self.totalPage=totalPage
		self.paddockList=paddockList
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage
if TYPE_CHECKING:
	...
class GuildSummaryRequestMessage(PaginationRequestAbstractMessage):
	def __init__(self, nameFilter:str, criterionFilter:list[int], languagesFilter:list[int], recruitmentTypeFilter:list[int], minLevelFilter:int, maxLevelFilter:int, minPlayerLevelFilter:int, maxPlayerLevelFilter:int, minSuccessFilter:int, maxSuccessFilter:int, sortType:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.nameFilter=nameFilter
		self.criterionFilter=criterionFilter
		self.languagesFilter=languagesFilter
		self.recruitmentTypeFilter=recruitmentTypeFilter
		self.minLevelFilter=minLevelFilter
		self.maxLevelFilter=maxLevelFilter
		self.minPlayerLevelFilter=minPlayerLevelFilter
		self.maxPlayerLevelFilter=maxPlayerLevelFilter
		self.minSuccessFilter=minSuccessFilter
		self.maxSuccessFilter=maxSuccessFilter
		self.sortType=sortType
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage
if TYPE_CHECKING:
	...
class AllianceSummaryRequestMessage(PaginationRequestAbstractMessage):
	def __init__(self, filterType:int, textFilter:str, criterionFilter:list[int], sortType:int, languagesFilter:list[int], recruitmentTypeFilter:list[int], minPlayerLevelFilter:int, maxPlayerLevelFilter:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.filterType=filterType
		self.textFilter=textFilter
		self.criterionFilter=criterionFilter
		self.sortType=sortType
		self.languagesFilter=languagesFilter
		self.recruitmentTypeFilter=recruitmentTypeFilter
		self.minPlayerLevelFilter=minPlayerLevelFilter
		self.maxPlayerLevelFilter=maxPlayerLevelFilter
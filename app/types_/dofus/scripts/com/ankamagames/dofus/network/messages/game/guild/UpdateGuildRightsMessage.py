from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class UpdateGuildRightsMessage:
	def __init__(self, rankId:int, rights:list[int]):
		self.rankId=rankId
		self.rights=rights
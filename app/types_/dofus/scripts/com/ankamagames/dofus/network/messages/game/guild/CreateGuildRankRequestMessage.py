from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CreateGuildRankRequestMessage:
	def __init__(self, parentRankId:int, gfxId:int, name:str):
		self.parentRankId=parentRankId
		self.gfxId=gfxId
		self.name=name
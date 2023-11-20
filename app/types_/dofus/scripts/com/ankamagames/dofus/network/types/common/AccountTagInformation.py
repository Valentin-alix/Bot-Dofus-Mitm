from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AccountTagInformation:
	def __init__(self, nickname:str, tagNumber:str):
		self.nickname=nickname
		self.tagNumber=tagNumber
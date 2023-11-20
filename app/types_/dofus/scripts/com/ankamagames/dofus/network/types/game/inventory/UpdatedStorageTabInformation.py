from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class UpdatedStorageTabInformation:
	def __init__(self, name:str, tabNumber:int, picto:int, dropTypeLimitation:list[int]):
		self.name=name
		self.tabNumber=tabNumber
		self.picto=picto
		self.dropTypeLimitation=dropTypeLimitation
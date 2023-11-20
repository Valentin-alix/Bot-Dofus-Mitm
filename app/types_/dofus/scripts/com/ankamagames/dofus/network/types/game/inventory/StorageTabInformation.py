from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class StorageTabInformation:
	def __init__(self, name:str, tabNumber:int, picto:int, openRight:int, dropRight:int, takeRight:int, dropTypeLimitation:list[int]):
		self.name=name
		self.tabNumber=tabNumber
		self.picto=picto
		self.openRight=openRight
		self.dropRight=dropRight
		self.takeRight=takeRight
		self.dropTypeLimitation=dropTypeLimitation
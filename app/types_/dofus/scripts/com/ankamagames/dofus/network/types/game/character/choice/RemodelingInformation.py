from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class RemodelingInformation:
	def __init__(self, name:str, breed:int, sex:bool, cosmeticId:int, colors:list[int]):
		self.name=name
		self.breed=breed
		self.sex=sex
		self.cosmeticId=cosmeticId
		self.colors=colors
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterCreationRequestMessage:
	def __init__(self, name:str, breed:int, sex:bool, colors:list[int], cosmeticId:int):
		self.name=name
		self.breed=breed
		self.sex=sex
		self.colors=colors
		self.cosmeticId=cosmeticId
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeMountFreeFromPaddockMessage:
	def __init__(self, name:str, worldX:int, worldY:int, liberator:str):
		self.name=name
		self.worldX=worldX
		self.worldY=worldY
		self.liberator=liberator
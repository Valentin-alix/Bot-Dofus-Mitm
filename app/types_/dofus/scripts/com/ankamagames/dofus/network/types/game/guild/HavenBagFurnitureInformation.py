from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HavenBagFurnitureInformation:
	def __init__(self, cellId:int, funitureId:int, orientation:int):
		self.cellId=cellId
		self.funitureId=funitureId
		self.orientation=orientation
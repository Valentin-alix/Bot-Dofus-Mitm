from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HavenBagFurnituresRequestMessage:
	def __init__(self, cellIds:list[int], funitureIds:list[int], orientations:list[int]):
		self.cellIds=cellIds
		self.funitureIds=funitureIds
		self.orientations=orientations
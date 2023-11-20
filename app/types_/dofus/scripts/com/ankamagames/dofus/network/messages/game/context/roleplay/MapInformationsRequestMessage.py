from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MapInformationsRequestMessage:
	def __init__(self, mapId:float):
		self.mapId=mapId
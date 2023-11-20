from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SocialFightInfo:
	def __init__(self, fightId:int, fightType:int, mapId:float):
		self.fightId=fightId
		self.fightType=fightType
		self.mapId=mapId
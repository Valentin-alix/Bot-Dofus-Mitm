from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightFighterLightInformations:
	def __init__(self, id:float, wave:int, level:int, breed:int):
		self.id=id
		self.wave=wave
		self.level=level
		self.breed=breed
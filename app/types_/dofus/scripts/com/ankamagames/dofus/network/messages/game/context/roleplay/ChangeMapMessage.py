from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChangeMapMessage:
	def __init__(self, mapId:float, autopilot:bool):
		self.mapId=mapId
		self.autopilot=autopilot
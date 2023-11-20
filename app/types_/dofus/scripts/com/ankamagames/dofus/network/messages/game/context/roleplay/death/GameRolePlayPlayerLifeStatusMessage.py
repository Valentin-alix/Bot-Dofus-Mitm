from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayPlayerLifeStatusMessage:
	def __init__(self, state:int, phenixMapId:float):
		self.state=state
		self.phenixMapId=phenixMapId
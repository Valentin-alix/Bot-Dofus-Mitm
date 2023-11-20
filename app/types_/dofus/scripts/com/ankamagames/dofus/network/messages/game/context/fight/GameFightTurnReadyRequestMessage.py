from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightTurnReadyRequestMessage:
	def __init__(self, id:float):
		self.id=id
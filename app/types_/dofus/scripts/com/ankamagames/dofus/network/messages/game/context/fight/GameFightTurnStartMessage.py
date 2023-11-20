from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightTurnStartMessage:
	def __init__(self, id:float, waitTime:int):
		self.id=id
		self.waitTime=waitTime
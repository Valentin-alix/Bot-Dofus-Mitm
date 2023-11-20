from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightTurnReadyMessage:
	def __init__(self, isReady:bool):
		self.isReady=isReady
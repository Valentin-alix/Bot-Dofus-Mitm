from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightReadyMessage:
	def __init__(self, isReady:bool):
		self.isReady=isReady
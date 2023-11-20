from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightHumanReadyStateMessage:
	def __init__(self, characterId:int, isReady:bool):
		self.characterId=characterId
		self.isReady=isReady
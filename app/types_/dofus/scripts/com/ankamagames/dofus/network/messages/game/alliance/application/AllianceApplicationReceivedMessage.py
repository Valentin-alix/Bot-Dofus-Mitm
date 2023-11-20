from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceApplicationReceivedMessage:
	def __init__(self, playerName:str, playerId:int):
		self.playerName=playerName
		self.playerId=playerId
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MoodSmileyUpdateMessage:
	def __init__(self, accountId:int, playerId:int, smileyId:int):
		self.accountId=accountId
		self.playerId=playerId
		self.smileyId=smileyId
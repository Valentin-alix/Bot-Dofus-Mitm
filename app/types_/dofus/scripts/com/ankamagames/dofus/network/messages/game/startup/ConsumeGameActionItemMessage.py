from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ConsumeGameActionItemMessage:
	def __init__(self, actionId:int, characterId:int):
		self.actionId=actionId
		self.characterId=characterId
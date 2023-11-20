from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameServerInformations:
	def __init__(self, id:int, type:int, status:int, completion:int, charactersCount:int, charactersSlots:int, date:float):
		self.id=id
		self.type=type
		self.status=status
		self.completion=completion
		self.charactersCount=charactersCount
		self.charactersSlots=charactersSlots
		self.date=date
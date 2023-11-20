from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightTurnListMessage:
	def __init__(self, ids:list[float], deadsIds:list[float]):
		self.ids=ids
		self.deadsIds=deadsIds
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightTurnFinishMessage:
	def __init__(self, isAfk:bool):
		self.isAfk=isAfk
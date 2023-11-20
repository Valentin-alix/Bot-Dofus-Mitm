from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightOptionToggleMessage:
	def __init__(self, option:int):
		self.option=option
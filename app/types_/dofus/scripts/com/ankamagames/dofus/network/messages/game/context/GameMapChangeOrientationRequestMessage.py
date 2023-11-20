from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameMapChangeOrientationRequestMessage:
	def __init__(self, direction:int):
		self.direction=direction
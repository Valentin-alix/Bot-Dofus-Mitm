from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ActorOrientation:
	def __init__(self, id:float, direction:int):
		self.id=id
		self.direction=direction
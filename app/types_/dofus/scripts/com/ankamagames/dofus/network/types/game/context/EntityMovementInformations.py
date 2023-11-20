from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EntityMovementInformations:
	def __init__(self, id:int, steps:list[int]):
		self.id=id
		self.steps=steps
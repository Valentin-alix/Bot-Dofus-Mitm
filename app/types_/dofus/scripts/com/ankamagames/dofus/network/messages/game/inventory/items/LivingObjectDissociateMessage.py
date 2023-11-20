from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LivingObjectDissociateMessage:
	def __init__(self, livingUID:int, livingPosition:int):
		self.livingUID=livingUID
		self.livingPosition=livingPosition
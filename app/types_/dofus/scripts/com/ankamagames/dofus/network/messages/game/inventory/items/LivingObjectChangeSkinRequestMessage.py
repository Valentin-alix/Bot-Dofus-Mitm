from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LivingObjectChangeSkinRequestMessage:
	def __init__(self, livingUID:int, livingPosition:int, skinId:int):
		self.livingUID=livingUID
		self.livingPosition=livingPosition
		self.skinId=skinId
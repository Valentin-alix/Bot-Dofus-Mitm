from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LifePointsRegenBeginMessage:
	def __init__(self, regenRate:int):
		self.regenRate=regenRate
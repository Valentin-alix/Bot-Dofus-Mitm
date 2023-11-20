from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameActionFightCastOnTargetRequestMessage:
	def __init__(self, spellId:int, targetId:float):
		self.spellId=spellId
		self.targetId=targetId
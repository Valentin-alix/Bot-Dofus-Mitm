from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightEffectTriggerCount:
	def __init__(self, effectId:int, targetId:float, count:int):
		self.effectId=effectId
		self.targetId=targetId
		self.count=count
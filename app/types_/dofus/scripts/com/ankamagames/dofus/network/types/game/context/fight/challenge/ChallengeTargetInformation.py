from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChallengeTargetInformation:
	def __init__(self, targetId:float, targetCell:int):
		self.targetId=targetId
		self.targetCell=targetCell
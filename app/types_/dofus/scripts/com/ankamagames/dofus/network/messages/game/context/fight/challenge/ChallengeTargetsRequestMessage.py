from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChallengeTargetsRequestMessage:
	def __init__(self, challengeId:int):
		self.challengeId=challengeId
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChallengeResultMessage:
	def __init__(self, challengeId:int, success:bool):
		self.challengeId=challengeId
		self.success=success
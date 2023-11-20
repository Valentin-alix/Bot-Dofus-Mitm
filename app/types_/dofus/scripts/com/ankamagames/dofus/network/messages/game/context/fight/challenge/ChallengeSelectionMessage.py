from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChallengeSelectionMessage:
	def __init__(self, challengeId:int):
		self.challengeId=challengeId
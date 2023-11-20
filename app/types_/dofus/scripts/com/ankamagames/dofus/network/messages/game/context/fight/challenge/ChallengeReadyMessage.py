from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChallengeReadyMessage:
	def __init__(self, challengeMod:int):
		self.challengeMod=challengeMod
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MoodSmileyRequestMessage:
	def __init__(self, smileyId:int):
		self.smileyId=smileyId
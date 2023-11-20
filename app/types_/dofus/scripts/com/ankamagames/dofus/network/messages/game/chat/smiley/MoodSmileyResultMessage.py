from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MoodSmileyResultMessage:
	def __init__(self, resultCode:int, smileyId:int):
		self.resultCode=resultCode
		self.smileyId=smileyId
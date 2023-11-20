from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DiceRollRequestMessage:
	def __init__(self, dice:int, faces:int, channel:int):
		self.dice=dice
		self.faces=faces
		self.channel=channel
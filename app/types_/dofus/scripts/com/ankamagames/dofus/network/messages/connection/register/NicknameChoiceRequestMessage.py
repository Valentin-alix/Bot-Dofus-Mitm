from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NicknameChoiceRequestMessage:
	def __init__(self, nickname:str):
		self.nickname=nickname
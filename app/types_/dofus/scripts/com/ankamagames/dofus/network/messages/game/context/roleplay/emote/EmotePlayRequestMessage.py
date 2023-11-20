from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EmotePlayRequestMessage:
	def __init__(self, emoteId:int):
		self.emoteId=emoteId
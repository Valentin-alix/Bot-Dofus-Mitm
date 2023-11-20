from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EmotePlayAbstractMessage:
	def __init__(self, emoteId:int, emoteStartTime:float):
		self.emoteId=emoteId
		self.emoteStartTime=emoteStartTime
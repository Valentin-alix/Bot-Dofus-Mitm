from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChatAbstractServerMessage:
	def __init__(self, channel:int, content:str, timestamp:int, fingerprint:str):
		self.channel=channel
		self.content=content
		self.timestamp=timestamp
		self.fingerprint=fingerprint
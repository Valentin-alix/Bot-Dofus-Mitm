from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BasicAckMessage:
	def __init__(self, seq:int, lastPacketId:int):
		self.seq=seq
		self.lastPacketId=lastPacketId
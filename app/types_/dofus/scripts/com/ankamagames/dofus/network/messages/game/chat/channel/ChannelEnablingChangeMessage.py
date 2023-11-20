from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChannelEnablingChangeMessage:
	def __init__(self, channel:int, enable:bool):
		self.channel=channel
		self.enable=enable
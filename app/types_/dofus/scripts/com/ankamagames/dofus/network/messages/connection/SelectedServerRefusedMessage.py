from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SelectedServerRefusedMessage:
	def __init__(self, serverId:int, error:int, serverStatus:int):
		self.serverId=serverId
		self.error=error
		self.serverStatus=serverStatus
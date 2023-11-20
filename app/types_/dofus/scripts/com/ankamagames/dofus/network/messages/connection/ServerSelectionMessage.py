from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ServerSelectionMessage:
	def __init__(self, serverId:int):
		self.serverId=serverId
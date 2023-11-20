from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaSwitchToFightServerMessage:
	def __init__(self, address:str, ports:list[int], token:str):
		self.address=address
		self.ports=ports
		self.token=token
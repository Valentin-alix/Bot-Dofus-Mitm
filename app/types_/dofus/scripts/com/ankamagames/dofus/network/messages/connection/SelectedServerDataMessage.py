from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SelectedServerDataMessage:
	def __init__(self, serverId:int, address:str, ports:list[int], canCreateNewCharacter:bool, ticket:list[int]):
		self.serverId=serverId
		self.address=address
		self.ports=ports
		self.canCreateNewCharacter=canCreateNewCharacter
		self.ticket=ticket
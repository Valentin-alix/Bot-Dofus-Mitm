from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
class ServersListMessage:
	def __init__(self, servers:list[GameServerInformations], canCreateNewCharacter:bool):
		self.servers=servers
		self.canCreateNewCharacter=canCreateNewCharacter
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
class ServerStatusUpdateMessage:
	def __init__(self, server:GameServerInformations):
		self.server=server
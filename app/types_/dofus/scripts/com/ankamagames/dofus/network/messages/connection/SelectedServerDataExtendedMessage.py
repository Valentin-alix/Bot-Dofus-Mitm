from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import SelectedServerDataMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations
class SelectedServerDataExtendedMessage(SelectedServerDataMessage):
	def __init__(self, servers:list[GameServerInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.servers=servers
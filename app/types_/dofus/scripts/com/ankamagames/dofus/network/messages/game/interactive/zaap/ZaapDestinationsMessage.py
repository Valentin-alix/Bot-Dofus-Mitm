from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.interactive.zaap.TeleportDestinationsMessage import TeleportDestinationsMessage
if TYPE_CHECKING:
	...
class ZaapDestinationsMessage(TeleportDestinationsMessage):
	def __init__(self, spawnMapId:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.spawnMapId=spawnMapId
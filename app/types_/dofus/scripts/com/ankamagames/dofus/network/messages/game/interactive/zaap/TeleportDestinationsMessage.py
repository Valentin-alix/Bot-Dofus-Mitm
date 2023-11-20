from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.zaap.TeleportDestination import TeleportDestination
class TeleportDestinationsMessage:
	def __init__(self, type:int, destinations:list[TeleportDestination]):
		self.type=type
		self.destinations=destinations
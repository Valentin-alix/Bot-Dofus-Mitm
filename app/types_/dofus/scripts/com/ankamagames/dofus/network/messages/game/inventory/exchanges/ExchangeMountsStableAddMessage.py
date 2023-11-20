from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
class ExchangeMountsStableAddMessage:
	def __init__(self, mountDescription:list[MountClientData]):
		self.mountDescription=mountDescription
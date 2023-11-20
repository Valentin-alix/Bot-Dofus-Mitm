from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
class MountSetMessage:
	def __init__(self, mountData:MountClientData):
		self.mountData=mountData
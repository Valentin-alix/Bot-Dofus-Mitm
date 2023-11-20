from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
class HavenBagRoomUpdateMessage:
	def __init__(self, action:int, roomsPreview:list[HavenBagRoomPreviewInformation]):
		self.action=action
		self.roomsPreview=roomsPreview
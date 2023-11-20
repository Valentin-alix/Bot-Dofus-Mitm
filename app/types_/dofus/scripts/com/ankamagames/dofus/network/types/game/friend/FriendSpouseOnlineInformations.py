from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations
if TYPE_CHECKING:
	...
class FriendSpouseOnlineInformations(FriendSpouseInformations):
	def __init__(self, mapId:float, subAreaId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.mapId=mapId
		self.subAreaId=subAreaId
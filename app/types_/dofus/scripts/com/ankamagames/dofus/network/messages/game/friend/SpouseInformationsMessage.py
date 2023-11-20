from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations
class SpouseInformationsMessage:
	def __init__(self, spouse:FriendSpouseInformations):
		self.spouse=spouse
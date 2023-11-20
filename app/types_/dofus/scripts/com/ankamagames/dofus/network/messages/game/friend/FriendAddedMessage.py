from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations
class FriendAddedMessage:
	def __init__(self, friendAdded:FriendInformations):
		self.friendAdded=friendAdded
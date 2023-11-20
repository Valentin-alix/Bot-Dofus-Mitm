from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations
class FriendsListMessage:
	def __init__(self, friendsList:list[FriendInformations]):
		self.friendsList=friendsList
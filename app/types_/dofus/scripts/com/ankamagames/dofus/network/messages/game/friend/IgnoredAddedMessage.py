from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations
class IgnoredAddedMessage:
	def __init__(self, ignoreAdded:IgnoredInformations, session:bool):
		self.ignoreAdded=ignoreAdded
		self.session=session
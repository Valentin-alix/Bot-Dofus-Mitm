from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation
class AcquaintanceAddedMessage:
	def __init__(self, acquaintanceAdded:AcquaintanceInformation):
		self.acquaintanceAdded=acquaintanceAdded
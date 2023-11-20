from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
class FriendDeleteResultMessage:
	def __init__(self, success:bool, tag:AccountTagInformation):
		self.success=success
		self.tag=tag
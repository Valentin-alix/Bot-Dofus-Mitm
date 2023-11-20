from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
class IgnoredDeleteResultMessage:
	def __init__(self, tag:AccountTagInformation):
		self.tag=tag
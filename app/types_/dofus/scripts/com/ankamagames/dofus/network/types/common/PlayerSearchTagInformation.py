from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
class PlayerSearchTagInformation(AbstractPlayerSearchInformation):
	def __init__(self, tag:AccountTagInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.tag=tag
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
class BasicWhoIsRequestMessage:
	def __init__(self, verbose:bool, target:AbstractPlayerSearchInformation):
		self.verbose=verbose
		self.target=target
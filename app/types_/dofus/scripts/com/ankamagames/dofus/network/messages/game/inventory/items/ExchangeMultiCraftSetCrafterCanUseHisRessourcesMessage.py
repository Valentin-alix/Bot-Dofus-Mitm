from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage:
	def __init__(self, allow:bool):
		self.allow=allow
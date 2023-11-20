from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeMultiCraftCrafterCanUseHisRessourcesMessage:
	def __init__(self, allowed:bool):
		self.allowed=allowed
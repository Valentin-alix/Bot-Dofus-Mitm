from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class StartListenTaxCollectorUpdatesMessage:
	def __init__(self, taxCollectorId:float):
		self.taxCollectorId=taxCollectorId
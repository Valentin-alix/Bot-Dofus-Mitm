from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class KnownZaapListMessage:
	def __init__(self, destinations:list[float]):
		self.destinations=destinations
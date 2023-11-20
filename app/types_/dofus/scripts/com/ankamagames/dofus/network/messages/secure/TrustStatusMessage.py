from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TrustStatusMessage:
	def __init__(self, certified:bool):
		self.certified=certified
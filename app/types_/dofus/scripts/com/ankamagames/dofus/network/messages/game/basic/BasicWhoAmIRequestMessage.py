from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BasicWhoAmIRequestMessage:
	def __init__(self, verbose:bool):
		self.verbose=verbose
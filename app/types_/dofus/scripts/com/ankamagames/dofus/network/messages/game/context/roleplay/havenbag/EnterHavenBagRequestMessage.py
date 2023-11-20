from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EnterHavenBagRequestMessage:
	def __init__(self, havenBagOwner:int):
		self.havenBagOwner=havenBagOwner
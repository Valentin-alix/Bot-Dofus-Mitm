from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeMountsStableRemoveMessage:
	def __init__(self, mountsId:list[int]):
		self.mountsId=mountsId
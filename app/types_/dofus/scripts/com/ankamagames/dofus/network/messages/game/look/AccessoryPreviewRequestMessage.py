from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AccessoryPreviewRequestMessage:
	def __init__(self, genericId:list[int]):
		self.genericId=genericId
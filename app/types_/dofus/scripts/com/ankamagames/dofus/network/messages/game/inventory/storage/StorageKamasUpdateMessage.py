from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class StorageKamasUpdateMessage:
	def __init__(self, kamasTotal:int):
		self.kamasTotal=kamasTotal
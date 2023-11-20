from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HaapiConfirmationRequestMessage:
	def __init__(self, kamas:int, ogrines:int, rate:int, action:int):
		self.kamas=kamas
		self.ogrines=ogrines
		self.rate=rate
		self.action=action
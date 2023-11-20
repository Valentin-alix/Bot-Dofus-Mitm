from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ClientKeyMessage:
	def __init__(self, key:str):
		self.key=key
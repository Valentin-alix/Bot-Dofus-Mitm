from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HelloConnectMessage:
	def __init__(self, salt:str, key:list[int]):
		self.salt=salt
		self.key=key
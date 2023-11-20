from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HaapiTokenMessage:
	def __init__(self, token:str):
		self.token=token
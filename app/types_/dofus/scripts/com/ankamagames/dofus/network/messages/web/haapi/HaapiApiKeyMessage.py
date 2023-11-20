from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HaapiApiKeyMessage:
	def __init__(self, token:str):
		self.token=token
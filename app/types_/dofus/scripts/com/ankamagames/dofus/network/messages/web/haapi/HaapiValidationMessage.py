from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HaapiValidationMessage:
	def __init__(self, action:int, code:int):
		self.action=action
		self.code=code
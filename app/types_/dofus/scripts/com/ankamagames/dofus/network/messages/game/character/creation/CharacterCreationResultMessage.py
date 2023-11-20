from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterCreationResultMessage:
	def __init__(self, result:int, reason:int):
		self.result=result
		self.reason=reason
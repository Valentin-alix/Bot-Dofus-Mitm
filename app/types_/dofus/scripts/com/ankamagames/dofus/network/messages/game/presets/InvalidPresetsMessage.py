from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class InvalidPresetsMessage:
	def __init__(self, presetIds:list[int]):
		self.presetIds=presetIds
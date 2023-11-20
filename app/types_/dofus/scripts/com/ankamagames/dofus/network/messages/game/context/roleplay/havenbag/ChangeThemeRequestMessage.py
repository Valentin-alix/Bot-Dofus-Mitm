from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChangeThemeRequestMessage:
	def __init__(self, theme:int):
		self.theme=theme
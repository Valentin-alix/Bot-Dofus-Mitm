from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachSavedMessage:
	def __init__(self, saved:bool):
		self.saved=saved
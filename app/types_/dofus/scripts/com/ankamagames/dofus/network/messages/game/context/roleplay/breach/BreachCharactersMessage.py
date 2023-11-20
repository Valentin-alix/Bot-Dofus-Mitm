from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachCharactersMessage:
	def __init__(self, characters:list[int]):
		self.characters=characters
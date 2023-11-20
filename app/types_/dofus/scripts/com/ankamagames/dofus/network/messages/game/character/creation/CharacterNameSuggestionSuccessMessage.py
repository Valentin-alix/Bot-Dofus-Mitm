from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterNameSuggestionSuccessMessage:
	def __init__(self, suggestion:str):
		self.suggestion=suggestion
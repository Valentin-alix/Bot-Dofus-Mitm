from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterDeletionPrepareRequestMessage:
	def __init__(self, characterId:int):
		self.characterId=characterId
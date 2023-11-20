from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterDeletionRequestMessage:
	def __init__(self, characterId:int, secretAnswerHash:str):
		self.characterId=characterId
		self.secretAnswerHash=secretAnswerHash
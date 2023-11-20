from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterDeletionPrepareMessage:
	def __init__(self, characterId:int, characterName:str, secretQuestion:str, needSecretAnswer:bool):
		self.characterId=characterId
		self.characterName=characterName
		self.secretQuestion=secretQuestion
		self.needSecretAnswer=needSecretAnswer
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterExperienceGainMessage:
	def __init__(self, experienceCharacter:int, experienceMount:int, experienceGuild:int, experienceIncarnation:int):
		self.experienceCharacter=experienceCharacter
		self.experienceMount=experienceMount
		self.experienceGuild=experienceGuild
		self.experienceIncarnation=experienceIncarnation
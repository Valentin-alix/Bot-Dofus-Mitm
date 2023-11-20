from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData
if TYPE_CHECKING:
	...
class FightResultExperienceData(FightResultAdditionalData):
	def __init__(self, experience:int, experienceLevelFloor:int, experienceNextLevelFloor:int, experienceFightDelta:int, experienceForGuild:int, experienceForMount:int, rerollExperienceMul:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.experience=experience
		self.experienceLevelFloor=experienceLevelFloor
		self.experienceNextLevelFloor=experienceNextLevelFloor
		self.experienceFightDelta=experienceFightDelta
		self.experienceForGuild=experienceForGuild
		self.experienceForMount=experienceForMount
		self.rerollExperienceMul=rerollExperienceMul
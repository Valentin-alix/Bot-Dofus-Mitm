from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.alignment.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.spellmodifier.SpellModifierMessage import SpellModifierMessage
class CharacterCharacteristicsInformations:
	def __init__(self, experience:int, experienceLevelFloor:int, experienceNextLevelFloor:int, experienceBonusLimit:int, kamas:int, alignmentInfos:ActorExtendedAlignmentInformations, criticalHitWeapon:int, characteristics:list[CharacterCharacteristic], spellModifiers:list[SpellModifierMessage], probationTime:float):
		self.experience=experience
		self.experienceLevelFloor=experienceLevelFloor
		self.experienceNextLevelFloor=experienceNextLevelFloor
		self.experienceBonusLimit=experienceBonusLimit
		self.kamas=kamas
		self.alignmentInfos=alignmentInfos
		self.criticalHitWeapon=criticalHitWeapon
		self.characteristics=characteristics
		self.spellModifiers=spellModifiers
		self.probationTime=probationTime
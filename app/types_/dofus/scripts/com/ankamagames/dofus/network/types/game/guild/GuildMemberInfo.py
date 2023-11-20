from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.SocialMember import SocialMember
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.guild.note.PlayerNote import PlayerNote
class GuildMemberInfo(SocialMember):
	def __init__(self, givenExperience:int, experienceGivenPercent:int, alignmentSide:int, moodSmileyId:int, achievementPoints:int, havenBagShared:bool, note:PlayerNote, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.givenExperience=givenExperience
		self.experienceGivenPercent=experienceGivenPercent
		self.alignmentSide=alignmentSide
		self.moodSmileyId=moodSmileyId
		self.achievementPoints=achievementPoints
		self.havenBagShared=havenBagShared
		self.note=note
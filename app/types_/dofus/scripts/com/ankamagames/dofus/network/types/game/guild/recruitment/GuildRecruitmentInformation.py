from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.recruitment.SocialRecruitmentInformation import SocialRecruitmentInformation
if TYPE_CHECKING:
	...
class GuildRecruitmentInformation(SocialRecruitmentInformation):
	def __init__(self, minSuccess:int, minSuccessFacultative:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.minSuccess=minSuccess
		self.minSuccessFacultative=minSuccessFacultative
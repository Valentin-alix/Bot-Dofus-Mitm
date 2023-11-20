from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.recruitment.SocialRecruitmentInformation import SocialRecruitmentInformation
if TYPE_CHECKING:
	...
class AllianceRecruitmentInformation(SocialRecruitmentInformation):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...
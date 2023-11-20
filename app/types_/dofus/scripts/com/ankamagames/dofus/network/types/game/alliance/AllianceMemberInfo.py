from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.SocialMember import SocialMember
if TYPE_CHECKING:
	...
class AllianceMemberInfo(SocialMember):
	def __init__(self, avaRoleId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.avaRoleId=avaRoleId
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.fight.SocialFightInfo import SocialFightInfo
class SocialFightLeaveRequestMessage:
	def __init__(self, socialFightInfo:SocialFightInfo):
		self.socialFightInfo=socialFightInfo
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos
if TYPE_CHECKING:
	...
class BasicAllianceInformations(AbstractSocialGroupInfos):
	def __init__(self, allianceId:int, allianceTag:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.allianceId=allianceId
		self.allianceTag=allianceTag
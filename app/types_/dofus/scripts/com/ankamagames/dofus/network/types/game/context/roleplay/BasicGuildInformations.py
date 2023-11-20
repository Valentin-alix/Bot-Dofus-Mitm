from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos
if TYPE_CHECKING:
	...
class BasicGuildInformations(AbstractSocialGroupInfos):
	def __init__(self, guildId:int, guildName:str, guildLevel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guildId=guildId
		self.guildName=guildName
		self.guildLevel=guildLevel
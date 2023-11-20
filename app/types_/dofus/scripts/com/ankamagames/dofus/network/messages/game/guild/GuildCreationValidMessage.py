from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.SocialEmblem import SocialEmblem
class GuildCreationValidMessage:
	def __init__(self, guildName:str, guildEmblem:SocialEmblem):
		self.guildName=guildName
		self.guildEmblem=guildEmblem
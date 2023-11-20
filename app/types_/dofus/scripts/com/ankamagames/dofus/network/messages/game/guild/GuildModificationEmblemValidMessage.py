from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.SocialEmblem import SocialEmblem
class GuildModificationEmblemValidMessage:
	def __init__(self, guildEmblem:SocialEmblem):
		self.guildEmblem=guildEmblem
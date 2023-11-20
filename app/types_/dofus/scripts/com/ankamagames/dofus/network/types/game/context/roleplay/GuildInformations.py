from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.SocialEmblem import SocialEmblem
class GuildInformations(BasicGuildInformations):
	def __init__(self, guildEmblem:SocialEmblem, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guildEmblem=guildEmblem
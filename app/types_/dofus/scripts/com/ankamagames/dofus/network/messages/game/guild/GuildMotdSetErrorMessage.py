from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetErrorMessage import SocialNoticeSetErrorMessage
if TYPE_CHECKING:
	...
class GuildMotdSetErrorMessage(SocialNoticeSetErrorMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...
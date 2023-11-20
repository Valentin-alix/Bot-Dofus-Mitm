from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.fight.GameFightResumeMessage import GameFightResumeMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo
class GameFightResumeWithSlavesMessage(GameFightResumeMessage):
	def __init__(self, slavesInfo:list[GameFightResumeSlaveInfo], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.slavesInfo=slavesInfo
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
class GameActionFightSummonMessage(AbstractGameActionMessage):
	def __init__(self, summons:list[GameFightFighterInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.summons=summons
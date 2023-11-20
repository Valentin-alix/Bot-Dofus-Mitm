from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameContextSummonsInformation import GameContextSummonsInformation
class GameActionFightMultipleSummonMessage(AbstractGameActionMessage):
	def __init__(self, summons:list[GameContextSummonsInformation], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.summons=summons
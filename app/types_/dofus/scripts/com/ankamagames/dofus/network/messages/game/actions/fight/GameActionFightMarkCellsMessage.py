from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
class GameActionFightMarkCellsMessage(AbstractGameActionMessage):
	def __init__(self, mark:GameActionMark, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.mark=mark
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellMessage import GameActionFightDispellMessage
if TYPE_CHECKING:
	...
class GameActionFightDispellSpellMessage(GameActionFightDispellMessage):
	def __init__(self, spellId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.spellId=spellId
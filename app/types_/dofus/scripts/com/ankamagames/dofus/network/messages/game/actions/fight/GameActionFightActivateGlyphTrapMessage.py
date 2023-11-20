from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	...
class GameActionFightActivateGlyphTrapMessage(AbstractGameActionMessage):
	def __init__(self, markId:int, active:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.markId=markId
		self.active=active
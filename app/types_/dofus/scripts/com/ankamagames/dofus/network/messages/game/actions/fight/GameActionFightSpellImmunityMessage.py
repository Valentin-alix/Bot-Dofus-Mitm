from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	...
class GameActionFightSpellImmunityMessage(AbstractGameActionMessage):
	def __init__(self, targetId:float, spellId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.targetId=targetId
		self.spellId=spellId
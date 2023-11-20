from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	...
class GameActionFightDispellMessage(AbstractGameActionMessage):
	def __init__(self, targetId:float, verboseCast:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.targetId=targetId
		self.verboseCast=verboseCast
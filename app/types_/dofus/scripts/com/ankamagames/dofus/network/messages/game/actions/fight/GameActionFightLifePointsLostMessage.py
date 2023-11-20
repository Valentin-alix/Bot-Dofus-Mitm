from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	...
class GameActionFightLifePointsLostMessage(AbstractGameActionMessage):
	def __init__(self, targetId:float, loss:int, permanentDamages:int, elementId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.targetId=targetId
		self.loss=loss
		self.permanentDamages=permanentDamages
		self.elementId=elementId
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect
class FightDispellableEffectExtendedInformations:
	def __init__(self, actionId:int, sourceId:float, effect:AbstractFightDispellableEffect):
		self.actionId=actionId
		self.sourceId=sourceId
		self.effect=effect
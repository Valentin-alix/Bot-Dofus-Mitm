from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect
class GameActionFightDispellableEffectMessage(AbstractGameActionMessage):
	def __init__(self, effect:AbstractFightDispellableEffect, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.effect=effect
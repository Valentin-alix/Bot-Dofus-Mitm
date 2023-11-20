from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect
if TYPE_CHECKING:
	...
class FightTemporaryBoostEffect(AbstractFightDispellableEffect):
	def __init__(self, delta:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.delta=delta
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect
if TYPE_CHECKING:
	...
class FightTriggeredEffect(AbstractFightDispellableEffect):
	def __init__(self, param1:int, param2:int, param3:int, delay:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.param1=param1
		self.param2=param2
		self.param3=param3
		self.delay=delay
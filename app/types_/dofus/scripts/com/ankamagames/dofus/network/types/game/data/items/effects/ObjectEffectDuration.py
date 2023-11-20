from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
if TYPE_CHECKING:
	...
class ObjectEffectDuration(ObjectEffect):
	def __init__(self, days:int, hours:int, minutes:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.days=days
		self.hours=hours
		self.minutes=minutes
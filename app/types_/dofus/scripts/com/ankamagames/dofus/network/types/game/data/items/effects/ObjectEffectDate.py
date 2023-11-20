from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
if TYPE_CHECKING:
	...
class ObjectEffectDate(ObjectEffect):
	def __init__(self, year:int, month:int, day:int, hour:int, minute:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.year=year
		self.month=month
		self.day=day
		self.hour=hour
		self.minute=minute
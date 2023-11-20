from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
if TYPE_CHECKING:
	...
class ObjectEffectMinMax(ObjectEffect):
	def __init__(self, min:int, max:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.min=min
		self.max=max
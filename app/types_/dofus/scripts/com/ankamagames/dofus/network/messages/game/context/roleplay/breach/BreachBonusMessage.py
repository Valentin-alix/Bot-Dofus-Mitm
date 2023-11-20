from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger
class BreachBonusMessage:
	def __init__(self, bonus:ObjectEffectInteger):
		self.bonus=bonus
from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
if TYPE_CHECKING:
	...
class InteractiveElementWithAgeBonus(InteractiveElement):
	def __init__(self, ageBonus:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ageBonus=ageBonus
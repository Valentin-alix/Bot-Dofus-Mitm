from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch
if TYPE_CHECKING:
	...
class ExtendedLockedBreachBranch(ExtendedBreachBranch):
	def __init__(self, unlockPrice:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.unlockPrice=unlockPrice
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ForgettableSpellItem import ForgettableSpellItem
class ForgettableSpellListUpdateMessage:
	def __init__(self, action:int, spells:list[ForgettableSpellItem]):
		self.action=action
		self.spells=spells
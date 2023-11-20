from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
class SpellListMessage:
	def __init__(self, spellPrevisualization:bool, spells:list[SpellItem]):
		self.spellPrevisualization=spellPrevisualization
		self.spells=spells
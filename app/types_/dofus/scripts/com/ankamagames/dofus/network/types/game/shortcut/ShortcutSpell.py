from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut
if TYPE_CHECKING:
	...
class ShortcutSpell(Shortcut):
	def __init__(self, spellId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.spellId=spellId
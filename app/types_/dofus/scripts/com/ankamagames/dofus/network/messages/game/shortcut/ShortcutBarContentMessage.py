from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut
class ShortcutBarContentMessage:
	def __init__(self, barType:int, shortcuts:list[Shortcut]):
		self.barType=barType
		self.shortcuts=shortcuts
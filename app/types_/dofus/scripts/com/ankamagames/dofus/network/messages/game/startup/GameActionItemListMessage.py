from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.startup.GameActionItem import GameActionItem
class GameActionItemListMessage:
	def __init__(self, actions:list[GameActionItem]):
		self.actions=actions
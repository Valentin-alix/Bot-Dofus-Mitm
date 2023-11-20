from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch
class MapComplementaryInformationsBreachMessage(MapComplementaryInformationsDataMessage):
	def __init__(self, floor:int, room:int, infinityMode:int, branches:list[BreachBranch], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.floor=floor
		self.room=room
		self.infinityMode=infinityMode
		self.branches=branches
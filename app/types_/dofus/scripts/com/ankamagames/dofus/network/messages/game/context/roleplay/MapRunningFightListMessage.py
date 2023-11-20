from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightExternalInformations import FightExternalInformations
class MapRunningFightListMessage:
	def __init__(self, fights:list[FightExternalInformations]):
		self.fights=fights
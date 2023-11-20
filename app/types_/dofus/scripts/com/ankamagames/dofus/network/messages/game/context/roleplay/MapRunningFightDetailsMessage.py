from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
class MapRunningFightDetailsMessage:
	def __init__(self, fightId:int, attackers:list[GameFightFighterLightInformations], defenders:list[GameFightFighterLightInformations]):
		self.fightId=fightId
		self.attackers=attackers
		self.defenders=defenders
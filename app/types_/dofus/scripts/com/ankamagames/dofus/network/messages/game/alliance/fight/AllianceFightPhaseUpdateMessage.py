from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.fight.SocialFightInfo import SocialFightInfo
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightPhase import FightPhase
class AllianceFightPhaseUpdateMessage:
	def __init__(self, allianceFightInfo:SocialFightInfo, newPhase:FightPhase):
		self.allianceFightInfo=allianceFightInfo
		self.newPhase=newPhase
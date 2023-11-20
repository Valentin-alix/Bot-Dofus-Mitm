from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.fight.SocialFightInfo import SocialFightInfo
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightPhase import FightPhase
class AllianceFightStartedMessage:
	def __init__(self, allianceFightInfo:SocialFightInfo, phase:FightPhase):
		self.allianceFightInfo=allianceFightInfo
		self.phase=phase
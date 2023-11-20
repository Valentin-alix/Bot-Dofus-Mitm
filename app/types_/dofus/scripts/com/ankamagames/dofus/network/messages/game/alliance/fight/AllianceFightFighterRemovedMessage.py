from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.fight.SocialFightInfo import SocialFightInfo
class AllianceFightFighterRemovedMessage:
	def __init__(self, allianceFightInfo:SocialFightInfo, fighterId:int):
		self.allianceFightInfo=allianceFightInfo
		self.fighterId=fighterId
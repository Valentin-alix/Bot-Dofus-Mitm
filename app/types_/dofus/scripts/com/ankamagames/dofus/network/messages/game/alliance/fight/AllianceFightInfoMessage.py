from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.fight.SocialFight import SocialFight
class AllianceFightInfoMessage:
	def __init__(self, allianceFights:list[SocialFight]):
		self.allianceFights=allianceFights
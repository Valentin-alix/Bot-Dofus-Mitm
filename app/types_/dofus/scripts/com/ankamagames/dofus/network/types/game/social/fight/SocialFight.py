from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.fight.SocialFightInfo import SocialFightInfo
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightPhase import FightPhase
class SocialFight:
	def __init__(self, socialFightInfo:SocialFightInfo, attackers:list[CharacterMinimalPlusLookInformations], defenders:list[CharacterMinimalPlusLookInformations], phase:FightPhase):
		self.socialFightInfo=socialFightInfo
		self.attackers=attackers
		self.defenders=defenders
		self.phase=phase
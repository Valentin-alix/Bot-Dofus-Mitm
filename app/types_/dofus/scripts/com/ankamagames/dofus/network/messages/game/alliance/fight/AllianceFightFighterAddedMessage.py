from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.fight.SocialFightInfo import SocialFightInfo
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
class AllianceFightFighterAddedMessage:
	def __init__(self, allianceFightInfo:SocialFightInfo, fighter:CharacterMinimalPlusLookInformations, team:int):
		self.allianceFightInfo=allianceFightInfo
		self.fighter=fighter
		self.team=team
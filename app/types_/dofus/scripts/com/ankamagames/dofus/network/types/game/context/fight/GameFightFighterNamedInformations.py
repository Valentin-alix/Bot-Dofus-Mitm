from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
class GameFightFighterNamedInformations(GameFightFighterInformations):
	def __init__(self, name:str, status:PlayerStatus, leagueId:int, ladderPosition:int, hiddenInPrefight:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name=name
		self.status=status
		self.leagueId=leagueId
		self.ladderPosition=ladderPosition
		self.hiddenInPrefight=hiddenInPrefight
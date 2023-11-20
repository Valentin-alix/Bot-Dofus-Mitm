from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer
class DungeonPartyFinderRoomContentUpdateMessage:
	def __init__(self, dungeonId:int, addedPlayers:list[DungeonPartyFinderPlayer], removedPlayersIds:list[int]):
		self.dungeonId=dungeonId
		self.addedPlayers=addedPlayers
		self.removedPlayersIds=removedPlayersIds
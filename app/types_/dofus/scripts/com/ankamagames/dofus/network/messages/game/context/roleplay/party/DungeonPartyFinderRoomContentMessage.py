from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer
class DungeonPartyFinderRoomContentMessage:
	def __init__(self, dungeonId:int, players:list[DungeonPartyFinderPlayer]):
		self.dungeonId=dungeonId
		self.players=players
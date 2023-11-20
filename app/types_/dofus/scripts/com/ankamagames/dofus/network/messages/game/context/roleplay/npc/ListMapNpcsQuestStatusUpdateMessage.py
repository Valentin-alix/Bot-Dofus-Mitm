from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.npc.MapNpcQuestInfo import MapNpcQuestInfo
class ListMapNpcsQuestStatusUpdateMessage:
	def __init__(self, mapInfo:list[MapNpcQuestInfo]):
		self.mapInfo=mapInfo
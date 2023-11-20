from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild
class GuildHouseUpdateInformationMessage:
	def __init__(self, housesInformations:HouseInformationsForGuild):
		self.housesInformations=housesInformations
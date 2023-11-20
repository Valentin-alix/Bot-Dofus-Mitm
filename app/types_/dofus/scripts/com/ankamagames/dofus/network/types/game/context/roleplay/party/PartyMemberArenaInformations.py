from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations
if TYPE_CHECKING:
	...
class PartyMemberArenaInformations(PartyMemberInformations):
	def __init__(self, rank:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.rank=rank
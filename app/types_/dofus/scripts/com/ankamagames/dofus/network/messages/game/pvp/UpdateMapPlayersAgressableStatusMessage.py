from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.pvp.AgressableStatusMessage import AgressableStatusMessage
class UpdateMapPlayersAgressableStatusMessage:
	def __init__(self, playerAvAMessages:list[AgressableStatusMessage]):
		self.playerAvAMessages=playerAvAMessages
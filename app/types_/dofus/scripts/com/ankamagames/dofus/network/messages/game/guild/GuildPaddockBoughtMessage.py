from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.PaddockContentInformations import PaddockContentInformations
class GuildPaddockBoughtMessage:
	def __init__(self, paddockInfo:PaddockContentInformations):
		self.paddockInfo=paddockInfo
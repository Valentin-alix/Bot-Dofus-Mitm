from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.alliance.KothWinner import KothWinner
class KothEndMessage:
	def __init__(self, winner:KothWinner):
		self.winner=winner
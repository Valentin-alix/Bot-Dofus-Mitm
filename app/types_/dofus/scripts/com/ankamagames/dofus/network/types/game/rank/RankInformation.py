from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.rank.RankMinimalInformation import RankMinimalInformation
if TYPE_CHECKING:
	...
class RankInformation(RankMinimalInformation):
	def __init__(self, order:int, gfxId:int, modifiable:bool, rights:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.order=order
		self.gfxId=gfxId
		self.modifiable=modifiable
		self.rights=rights
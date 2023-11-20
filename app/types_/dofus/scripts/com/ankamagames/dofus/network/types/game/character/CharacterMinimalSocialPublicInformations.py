from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.RankPublicInformation import RankPublicInformation
class CharacterMinimalSocialPublicInformations(CharacterMinimalInformations):
	def __init__(self, rank:RankPublicInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.rank=rank
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.HavenBagFurnitureInformation import HavenBagFurnitureInformation
class HavenBagFurnituresMessage:
	def __init__(self, furnituresInfos:list[HavenBagFurnitureInformation]):
		self.furnituresInfos=furnituresInfos
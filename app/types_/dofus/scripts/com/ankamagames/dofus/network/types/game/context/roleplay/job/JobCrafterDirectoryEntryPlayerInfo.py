from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
class JobCrafterDirectoryEntryPlayerInfo:
	def __init__(self, playerId:int, playerName:str, alignmentSide:int, breed:int, sex:bool, isInWorkshop:bool, worldX:int, worldY:int, mapId:float, subAreaId:int, canCraftLegendary:bool, status:PlayerStatus):
		self.playerId=playerId
		self.playerName=playerName
		self.alignmentSide=alignmentSide
		self.breed=breed
		self.sex=sex
		self.isInWorkshop=isInWorkshop
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId
		self.canCraftLegendary=canCraftLegendary
		self.status=status
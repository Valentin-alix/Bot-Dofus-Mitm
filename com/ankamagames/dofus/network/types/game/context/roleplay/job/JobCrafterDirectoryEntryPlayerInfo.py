from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    


class JobCrafterDirectoryEntryPlayerInfo(NetworkMessage):
    playerId:int
    playerName:str
    alignmentSide:int
    breed:int
    sex:bool
    isInWorkshop:bool
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    canCraftLegendary:bool
    status:'PlayerStatus'
    

    def init(self, playerId_:int, playerName_:str, alignmentSide_:int, breed_:int, sex_:bool, isInWorkshop_:bool, worldX_:int, worldY_:int, mapId_:int, subAreaId_:int, canCraftLegendary_:bool, status_:'PlayerStatus'):
        self.playerId = playerId_
        self.playerName = playerName_
        self.alignmentSide = alignmentSide_
        self.breed = breed_
        self.sex = sex_
        self.isInWorkshop = isInWorkshop_
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        self.canCraftLegendary = canCraftLegendary_
        self.status = status_
        
        super().__init__()
    
    
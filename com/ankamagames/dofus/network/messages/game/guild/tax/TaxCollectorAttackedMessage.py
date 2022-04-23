from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class TaxCollectorAttackedMessage(NetworkMessage):
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    guild:'BasicGuildInformations'
    

    def init(self, firstNameId_:int, lastNameId_:int, worldX_:int, worldY_:int, mapId_:int, subAreaId_:int, guild_:'BasicGuildInformations'):
        self.firstNameId = firstNameId_
        self.lastNameId = lastNameId_
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        self.guild = guild_
        
        super().__init__()
    
    
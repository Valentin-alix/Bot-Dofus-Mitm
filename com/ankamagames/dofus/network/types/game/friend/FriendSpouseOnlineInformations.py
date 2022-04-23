from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class FriendSpouseOnlineInformations(FriendSpouseInformations):
    mapId:int
    subAreaId:int
    inFight:bool
    followSpouse:bool
    inFight:bool
    followSpouse:bool
    

    def init(self, mapId_:int, subAreaId_:int, inFight_:bool, followSpouse_:bool, spouseAccountId_:int, spouseId_:int, spouseName_:str, spouseLevel_:int, breed_:int, sex_:int, spouseEntityLook_:'EntityLook', guildInfo_:'GuildInformations', alignmentSide_:int):
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        self.inFight = inFight_
        self.followSpouse = followSpouse_
        
        super().__init__(spouseAccountId_, spouseId_, spouseName_, spouseLevel_, breed_, sex_, spouseEntityLook_, guildInfo_, alignmentSide_)
    
    
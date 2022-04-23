from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class FriendSpouseInformations(NetworkMessage):
    spouseAccountId:int
    spouseId:int
    spouseName:str
    spouseLevel:int
    breed:int
    sex:int
    spouseEntityLook:'EntityLook'
    guildInfo:'GuildInformations'
    alignmentSide:int
    

    def init(self, spouseAccountId_:int, spouseId_:int, spouseName_:str, spouseLevel_:int, breed_:int, sex_:int, spouseEntityLook_:'EntityLook', guildInfo_:'GuildInformations', alignmentSide_:int):
        self.spouseAccountId = spouseAccountId_
        self.spouseId = spouseId_
        self.spouseName = spouseName_
        self.spouseLevel = spouseLevel_
        self.breed = breed_
        self.sex = sex_
        self.spouseEntityLook = spouseEntityLook_
        self.guildInfo = guildInfo_
        self.alignmentSide = alignmentSide_
        
        super().__init__()
    
    
from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class PartyEntityMemberInformation(PartyEntityBaseInformation):
    initiative:int
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    

    def init(self, initiative_:int, lifePoints_:int, maxLifePoints_:int, prospecting_:int, regenRate_:int, indexId_:int, entityModelId_:int, entityLook_:'EntityLook'):
        self.initiative = initiative_
        self.lifePoints = lifePoints_
        self.maxLifePoints = maxLifePoints_
        self.prospecting = prospecting_
        self.regenRate = regenRate_
        
        super().__init__(indexId_, entityModelId_, entityLook_)
    
    
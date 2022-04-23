from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class PartyMemberInformations(CharacterBaseInformations):
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    initiative:int
    alignmentSide:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    status:'PlayerStatus'
    entities:list['PartyEntityBaseInformation']
    

    def init(self, lifePoints_:int, maxLifePoints_:int, prospecting_:int, regenRate_:int, initiative_:int, alignmentSide_:int, worldX_:int, worldY_:int, mapId_:int, subAreaId_:int, status_:'PlayerStatus', entities_:list['PartyEntityBaseInformation'], sex_:bool, entityLook_:'EntityLook', breed_:int, level_:int, name_:str, id_:int):
        self.lifePoints = lifePoints_
        self.maxLifePoints = maxLifePoints_
        self.prospecting = prospecting_
        self.regenRate = regenRate_
        self.initiative = initiative_
        self.alignmentSide = alignmentSide_
        self.worldX = worldX_
        self.worldY = worldY_
        self.mapId = mapId_
        self.subAreaId = subAreaId_
        self.status = status_
        self.entities = entities_
        
        super().__init__(sex_, entityLook_, breed_, level_, name_, id_)
    
    
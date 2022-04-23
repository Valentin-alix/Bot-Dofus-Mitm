from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class PartyMemberArenaInformations(PartyMemberInformations):
    rank:int
    

    def init(self, rank_:int, lifePoints_:int, maxLifePoints_:int, prospecting_:int, regenRate_:int, initiative_:int, alignmentSide_:int, worldX_:int, worldY_:int, mapId_:int, subAreaId_:int, status_:'PlayerStatus', entities_:list['PartyEntityBaseInformation'], sex_:bool, entityLook_:'EntityLook', breed_:int, level_:int, name_:str, id_:int):
        self.rank = rank_
        
        super().__init__(lifePoints_, maxLifePoints_, prospecting_, regenRate_, initiative_, alignmentSide_, worldX_, worldY_, mapId_, subAreaId_, status_, entities_, sex_, entityLook_, breed_, level_, name_, id_)
    
    
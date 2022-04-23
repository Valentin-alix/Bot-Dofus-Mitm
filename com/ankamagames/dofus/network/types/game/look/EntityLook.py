from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.SubEntity import SubEntity
    


class EntityLook(NetworkMessage):
    bonesId:int
    skins:list[int]
    indexedColors:list[int]
    scales:list[int]
    subentities:list['SubEntity']
    

    def init(self, bonesId_:int, skins_:list[int], indexedColors_:list[int], scales_:list[int], subentities_:list['SubEntity']):
        self.bonesId = bonesId_
        self.skins = skins_
        self.indexedColors = indexedColors_
        self.scales = scales_
        self.subentities = subentities_
        
        super().__init__()
    
    
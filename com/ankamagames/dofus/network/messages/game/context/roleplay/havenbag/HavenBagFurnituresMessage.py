from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.HavenBagFurnitureInformation import HavenBagFurnitureInformation
    


class HavenBagFurnituresMessage(NetworkMessage):
    furnituresInfos:list['HavenBagFurnitureInformation']
    

    def init(self, furnituresInfos_:list['HavenBagFurnitureInformation']):
        self.furnituresInfos = furnituresInfos_
        
        super().__init__()
    
    
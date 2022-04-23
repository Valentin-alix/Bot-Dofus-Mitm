from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class TaxCollectorAttackedResultMessage(NetworkMessage):
    deadOrAlive:bool
    basicInfos:'TaxCollectorBasicInformations'
    guild:'BasicGuildInformations'
    

    def init(self, deadOrAlive_:bool, basicInfos_:'TaxCollectorBasicInformations', guild_:'BasicGuildInformations'):
        self.deadOrAlive = deadOrAlive_
        self.basicInfos = basicInfos_
        self.guild = guild_
        
        super().__init__()
    
    
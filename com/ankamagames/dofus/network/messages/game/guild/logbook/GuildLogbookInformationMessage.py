from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
    from com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
    


class GuildLogbookInformationMessage(NetworkMessage):
    globalActivities:list['GuildLogbookEntryBasicInformation']
    chestActivities:list['GuildLogbookEntryBasicInformation']
    

    def init(self, globalActivities_:list['GuildLogbookEntryBasicInformation'], chestActivities_:list['GuildLogbookEntryBasicInformation']):
        self.globalActivities = globalActivities_
        self.chestActivities = chestActivities_
        
        super().__init__()
    
    
from com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
    


class GuildSummaryMessage(PaginationAnswerAbstractMessage):
    guilds:list['GuildFactSheetInformations']
    

    def init(self, guilds_:list['GuildFactSheetInformations'], offset_:int, count_:int, total_:int):
        self.guilds = guilds_
        
        super().__init__(offset_, count_, total_)
    
    
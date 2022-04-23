from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildRankPublicInformation import GuildRankPublicInformation
    


class CharacterMinimalGuildPublicInformations(CharacterMinimalInformations):
    rank:'GuildRankPublicInformation'
    

    def init(self, rank_:'GuildRankPublicInformation', level_:int, name_:str, id_:int):
        self.rank = rank_
        
        super().__init__(level_, name_, id_)
    
    
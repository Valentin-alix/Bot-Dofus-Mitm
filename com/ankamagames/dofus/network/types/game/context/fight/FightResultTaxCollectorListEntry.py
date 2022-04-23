from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultTaxCollectorListEntry(FightResultFighterListEntry):
    level:int
    guildInfo:'BasicGuildInformations'
    experienceForGuild:int
    

    def init(self, level_:int, guildInfo_:'BasicGuildInformations', experienceForGuild_:int, id_:int, alive_:bool, outcome_:int, wave_:int, rewards_:'FightLoot'):
        self.level = level_
        self.guildInfo = guildInfo_
        self.experienceForGuild = experienceForGuild_
        
        super().__init__(id_, alive_, outcome_, wave_, rewards_)
    
    
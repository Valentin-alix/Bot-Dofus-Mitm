from com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation


class GuildLevelUpActivity(GuildLogbookEntryBasicInformation):
    newGuildLevel:int
    

    def init(self, newGuildLevel_:int, id_:int, date_:int):
        self.newGuildLevel = newGuildLevel_
        
        super().__init__(id_, date_)
    
    
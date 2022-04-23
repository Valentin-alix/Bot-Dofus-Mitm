from com.ankamagames.dofus.network.types.game.guild.GuildRankMinimalInformation import GuildRankMinimalInformation


class GuildRankPublicInformation(GuildRankMinimalInformation):
    order:int
    gfxId:int
    

    def init(self, order_:int, gfxId_:int, id_:int, name_:str):
        self.order = order_
        self.gfxId = gfxId_
        
        super().__init__(id_, name_)
    
    
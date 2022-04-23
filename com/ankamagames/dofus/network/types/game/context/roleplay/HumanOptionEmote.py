from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionEmote(HumanOption):
    emoteId:int
    emoteStartTime:int
    

    def init(self, emoteId_:int, emoteStartTime_:int):
        self.emoteId = emoteId_
        self.emoteStartTime = emoteStartTime_
        
        super().__init__()
    
    
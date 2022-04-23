from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMassiveMessage(EmotePlayAbstractMessage):
    actorIds:list[int]
    

    def init(self, actorIds_:list[int], emoteId_:int, emoteStartTime_:int):
        self.actorIds = actorIds_
        
        super().__init__(emoteId_, emoteStartTime_)
    
    
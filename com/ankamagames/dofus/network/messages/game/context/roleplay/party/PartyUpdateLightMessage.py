from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyUpdateLightMessage(AbstractPartyEventMessage):
    id:int
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    

    def init(self, id_:int, lifePoints_:int, maxLifePoints_:int, prospecting_:int, regenRate_:int, partyId_:int):
        self.id = id_
        self.lifePoints = lifePoints_
        self.maxLifePoints = maxLifePoints_
        self.prospecting = prospecting_
        self.regenRate = regenRate_
        
        super().__init__(partyId_)
    
    
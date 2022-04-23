from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationMessage import PartyInvitationMessage


class PartyInvitationDungeonMessage(PartyInvitationMessage):
    dungeonId:int
    

    def init(self, dungeonId_:int, partyType_:int, partyName_:str, maxParticipants_:int, fromId_:int, fromName_:str, toId_:int, partyId_:int):
        self.dungeonId = dungeonId_
        
        super().__init__(partyType_, partyName_, maxParticipants_, fromId_, fromName_, toId_, partyId_)
    
    
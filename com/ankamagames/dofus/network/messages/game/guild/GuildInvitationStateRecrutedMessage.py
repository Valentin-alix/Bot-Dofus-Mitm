from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildInvitationStateRecrutedMessage(NetworkMessage):
    invitationState:int
    

    def init(self, invitationState_:int):
        self.invitationState = invitationState_
        
        super().__init__()
    
    
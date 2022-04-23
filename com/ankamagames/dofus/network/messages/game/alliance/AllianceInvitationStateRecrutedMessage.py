from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceInvitationStateRecrutedMessage(NetworkMessage):
    invitationState:int
    

    def init(self, invitationState_:int):
        self.invitationState = invitationState_
        
        super().__init__()
    
    
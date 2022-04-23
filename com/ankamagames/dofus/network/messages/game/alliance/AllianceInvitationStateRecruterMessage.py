from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceInvitationStateRecruterMessage(NetworkMessage):
    recrutedName:str
    invitationState:int
    

    def init(self, recrutedName_:str, invitationState_:int):
        self.recrutedName = recrutedName_
        self.invitationState = invitationState_
        
        super().__init__()
    
    
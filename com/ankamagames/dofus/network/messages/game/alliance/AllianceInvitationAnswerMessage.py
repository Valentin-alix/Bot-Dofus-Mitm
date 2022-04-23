from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceInvitationAnswerMessage(NetworkMessage):
    accept:bool
    

    def init(self, accept_:bool):
        self.accept = accept_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachInvitationRequestMessage(NetworkMessage):
    guests:list[int]
    

    def init(self, guests_:list[int]):
        self.guests = guests_
        
        super().__init__()
    
    
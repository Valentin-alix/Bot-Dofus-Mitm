from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AuthenticationTicketMessage(NetworkMessage):
    lang:str
    ticket:str
    

    def init(self, lang_:str, ticket_:str):
        self.lang = lang_
        self.ticket = ticket_
        
        super().__init__()
    
    
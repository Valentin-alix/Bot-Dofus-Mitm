from com.ankamagames.dofus.network.messages.authorized.AdminCommandMessage import AdminCommandMessage


class AdminQuietCommandMessage(AdminCommandMessage):
    

    def init(self, content_:str):
        
        super().__init__(content_)
    
    
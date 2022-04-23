from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage


class IdentificationFailedBannedMessage(IdentificationFailedMessage):
    banEndDate:int
    

    def init(self, banEndDate_:int, reason_:int):
        self.banEndDate = banEndDate_
        
        super().__init__(reason_)
    
    
from com.ankamagames.dofus.network.messages.debug.DebugInClientMessage import DebugInClientMessage


class ClientYouAreDrunkMessage(DebugInClientMessage):
    

    def init(self, level_:int, message_:str):
        
        super().__init__(level_, message_)
    
    
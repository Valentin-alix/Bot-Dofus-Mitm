from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableChangeCodeMessage import LockableChangeCodeMessage


class HouseLockFromInsideRequestMessage(LockableChangeCodeMessage):
    

    def init(self, code_:str):
        
        super().__init__(code_)
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountCapabilitiesMessage(NetworkMessage):
    accountId:int
    breedsVisible:int
    breedsAvailable:int
    status:int
    tutorialAvailable:bool
    canCreateNewCharacter:bool
    tutorialAvailable:bool
    canCreateNewCharacter:bool
    

    def init(self, accountId_:int, breedsVisible_:int, breedsAvailable_:int, status_:int, tutorialAvailable_:bool, canCreateNewCharacter_:bool):
        self.accountId = accountId_
        self.breedsVisible = breedsVisible_
        self.breedsAvailable = breedsAvailable_
        self.status = status_
        self.tutorialAvailable = tutorialAvailable_
        self.canCreateNewCharacter = canCreateNewCharacter_
        
        super().__init__()
    
    
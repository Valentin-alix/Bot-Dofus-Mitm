from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class PlayerStatusExtended(PlayerStatus):
    message:str
    

    def init(self, message_:str, statusId_:int):
        self.message = message_
        
        super().__init__(statusId_)
    
    
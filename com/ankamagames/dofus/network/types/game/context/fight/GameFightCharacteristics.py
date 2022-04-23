from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics
    


class GameFightCharacteristics(NetworkMessage):
    characteristics:'CharacterCharacteristics'
    summoner:int
    summoned:bool
    invisibilityState:int
    

    def init(self, characteristics_:'CharacterCharacteristics', summoner_:int, summoned_:bool, invisibilityState_:int):
        self.characteristics = characteristics_
        self.summoner = summoner_
        self.summoned = summoned_
        self.invisibilityState = invisibilityState_
        
        super().__init__()
    
    
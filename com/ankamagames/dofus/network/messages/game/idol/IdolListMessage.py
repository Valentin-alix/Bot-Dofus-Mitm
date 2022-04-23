from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.idol.PartyIdol import PartyIdol
    


class IdolListMessage(NetworkMessage):
    chosenIdols:list[int]
    partyChosenIdols:list[int]
    partyIdols:list['PartyIdol']
    

    def init(self, chosenIdols_:list[int], partyChosenIdols_:list[int], partyIdols_:list['PartyIdol']):
        self.chosenIdols = chosenIdols_
        self.partyChosenIdols = partyChosenIdols_
        self.partyIdols = partyIdols_
        
        super().__init__()
    
    
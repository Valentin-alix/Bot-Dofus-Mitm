from com.ankamagames.dofus.network.messages.game.character.replay.CharacterReplayRequestMessage import CharacterReplayRequestMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.choice.RemodelingInformation import RemodelingInformation
    


class CharacterReplayWithRemodelRequestMessage(CharacterReplayRequestMessage):
    remodel:'RemodelingInformation'
    

    def init(self, remodel_:'RemodelingInformation', characterId_:int):
        self.remodel = remodel_
        
        super().__init__(characterId_)
    
    
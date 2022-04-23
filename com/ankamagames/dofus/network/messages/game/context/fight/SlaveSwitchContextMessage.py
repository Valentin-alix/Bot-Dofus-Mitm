from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
    from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut
    


class SlaveSwitchContextMessage(NetworkMessage):
    masterId:int
    slaveId:int
    slaveTurn:int
    slaveSpells:list['SpellItem']
    slaveStats:'CharacterCharacteristicsInformations'
    shortcuts:list['Shortcut']
    

    def init(self, masterId_:int, slaveId_:int, slaveTurn_:int, slaveSpells_:list['SpellItem'], slaveStats_:'CharacterCharacteristicsInformations', shortcuts_:list['Shortcut']):
        self.masterId = masterId_
        self.slaveId = slaveId_
        self.slaveTurn = slaveTurn_
        self.slaveSpells = slaveSpells_
        self.slaveStats = slaveStats_
        self.shortcuts = shortcuts_
        
        super().__init__()
    
    
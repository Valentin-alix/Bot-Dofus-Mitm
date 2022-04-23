from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.alignment.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification
    


class CharacterCharacteristicsInformations(NetworkMessage):
    experience:int
    experienceLevelFloor:int
    experienceNextLevelFloor:int
    experienceBonusLimit:int
    kamas:int
    alignmentInfos:'ActorExtendedAlignmentInformations'
    criticalHitWeapon:int
    characteristics:list['CharacterCharacteristic']
    spellModifications:list['CharacterSpellModification']
    probationTime:int
    

    def init(self, experience_:int, experienceLevelFloor_:int, experienceNextLevelFloor_:int, experienceBonusLimit_:int, kamas_:int, alignmentInfos_:'ActorExtendedAlignmentInformations', criticalHitWeapon_:int, characteristics_:list['CharacterCharacteristic'], spellModifications_:list['CharacterSpellModification'], probationTime_:int):
        self.experience = experience_
        self.experienceLevelFloor = experienceLevelFloor_
        self.experienceNextLevelFloor = experienceNextLevelFloor_
        self.experienceBonusLimit = experienceBonusLimit_
        self.kamas = kamas_
        self.alignmentInfos = alignmentInfos_
        self.criticalHitWeapon = criticalHitWeapon_
        self.characteristics = characteristics_
        self.spellModifications = spellModifications_
        self.probationTime = probationTime_
        
        super().__init__()
    
    
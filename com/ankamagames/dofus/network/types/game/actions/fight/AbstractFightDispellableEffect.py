from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractFightDispellableEffect(NetworkMessage):
    uid:int
    targetId:int
    turnDuration:int
    dispelable:int
    spellId:int
    effectId:int
    parentBoostUid:int
    

    def init(self, uid_:int, targetId_:int, turnDuration_:int, dispelable_:int, spellId_:int, effectId_:int, parentBoostUid_:int):
        self.uid = uid_
        self.targetId = targetId_
        self.turnDuration = turnDuration_
        self.dispelable = dispelable_
        self.spellId = spellId_
        self.effectId = effectId_
        self.parentBoostUid = parentBoostUid_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActorRestrictionsInformations(NetworkMessage):
    cantBeAggressed:bool
    cantBeChallenged:bool
    cantTrade:bool
    cantBeAttackedByMutant:bool
    cantRun:bool
    forceSlowWalk:bool
    cantMinimize:bool
    cantMove:bool
    cantAggress:bool
    cantChallenge:bool
    cantExchange:bool
    cantAttack:bool
    cantChat:bool
    cantBeMerchant:bool
    cantUseObject:bool
    cantUseTaxCollector:bool
    cantUseInteractive:bool
    cantSpeakToNPC:bool
    cantChangeZone:bool
    cantAttackMonster:bool
    cantBeAggressed:bool
    cantBeChallenged:bool
    cantTrade:bool
    cantBeAttackedByMutant:bool
    cantRun:bool
    forceSlowWalk:bool
    cantMinimize:bool
    cantMove:bool
    cantAggress:bool
    cantChallenge:bool
    cantExchange:bool
    cantAttack:bool
    cantChat:bool
    cantBeMerchant:bool
    cantUseObject:bool
    cantUseTaxCollector:bool
    cantUseInteractive:bool
    cantSpeakToNPC:bool
    cantChangeZone:bool
    cantAttackMonster:bool
    

    def init(self, cantBeAggressed_:bool, cantBeChallenged_:bool, cantTrade_:bool, cantBeAttackedByMutant_:bool, cantRun_:bool, forceSlowWalk_:bool, cantMinimize_:bool, cantMove_:bool, cantAggress_:bool, cantChallenge_:bool, cantExchange_:bool, cantAttack_:bool, cantChat_:bool, cantBeMerchant_:bool, cantUseObject_:bool, cantUseTaxCollector_:bool, cantUseInteractive_:bool, cantSpeakToNPC_:bool, cantChangeZone_:bool, cantAttackMonster_:bool):
        self.cantBeAggressed = cantBeAggressed_
        self.cantBeChallenged = cantBeChallenged_
        self.cantTrade = cantTrade_
        self.cantBeAttackedByMutant = cantBeAttackedByMutant_
        self.cantRun = cantRun_
        self.forceSlowWalk = forceSlowWalk_
        self.cantMinimize = cantMinimize_
        self.cantMove = cantMove_
        self.cantAggress = cantAggress_
        self.cantChallenge = cantChallenge_
        self.cantExchange = cantExchange_
        self.cantAttack = cantAttack_
        self.cantChat = cantChat_
        self.cantBeMerchant = cantBeMerchant_
        self.cantUseObject = cantUseObject_
        self.cantUseTaxCollector = cantUseTaxCollector_
        self.cantUseInteractive = cantUseInteractive_
        self.cantSpeakToNPC = cantSpeakToNPC_
        self.cantChangeZone = cantChangeZone_
        self.cantAttackMonster = cantAttackMonster_
        
        super().__init__()
    
    
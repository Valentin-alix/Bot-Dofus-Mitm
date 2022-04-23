from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildInfosUpgradeMessage(NetworkMessage):
    maxTaxCollectorsCount:int
    taxCollectorsCount:int
    taxCollectorLifePoints:int
    taxCollectorDamagesBonuses:int
    taxCollectorPods:int
    taxCollectorProspecting:int
    taxCollectorWisdom:int
    boostPoints:int
    spellId:list[int]
    spellLevel:list[int]
    

    def init(self, maxTaxCollectorsCount_:int, taxCollectorsCount_:int, taxCollectorLifePoints_:int, taxCollectorDamagesBonuses_:int, taxCollectorPods_:int, taxCollectorProspecting_:int, taxCollectorWisdom_:int, boostPoints_:int, spellId_:list[int], spellLevel_:list[int]):
        self.maxTaxCollectorsCount = maxTaxCollectorsCount_
        self.taxCollectorsCount = taxCollectorsCount_
        self.taxCollectorLifePoints = taxCollectorLifePoints_
        self.taxCollectorDamagesBonuses = taxCollectorDamagesBonuses_
        self.taxCollectorPods = taxCollectorPods_
        self.taxCollectorProspecting = taxCollectorProspecting_
        self.taxCollectorWisdom = taxCollectorWisdom_
        self.boostPoints = boostPoints_
        self.spellId = spellId_
        self.spellLevel = spellLevel_
        
        super().__init__()
    
    
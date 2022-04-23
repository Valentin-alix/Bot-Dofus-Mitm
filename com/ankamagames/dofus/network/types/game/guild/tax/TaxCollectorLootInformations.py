from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations


class TaxCollectorLootInformations(TaxCollectorComplementaryInformations):
    kamas:int
    experience:int
    pods:int
    itemsValue:int
    

    def init(self, kamas_:int, experience_:int, pods_:int, itemsValue_:int):
        self.kamas = kamas_
        self.experience = experience_
        self.pods = pods_
        self.itemsValue = itemsValue_
        
        super().__init__()
    
    
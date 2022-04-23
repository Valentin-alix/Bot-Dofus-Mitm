from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FightLoot(NetworkMessage):
    objects:list[int]
    kamas:int
    

    def init(self, objects_:list[int], kamas_:int):
        self.objects = objects_
        self.kamas = kamas_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcDialogCreationMessage(NetworkMessage):
    mapId:int
    npcId:int
    

    def init(self, mapId_:int, npcId_:int):
        self.mapId = mapId_
        self.npcId = npcId_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcGenericActionRequestMessage(NetworkMessage):
    npcId:int
    npcActionId:int
    npcMapId:int
    

    def init(self, npcId_:int, npcActionId_:int, npcMapId_:int):
        self.npcId = npcId_
        self.npcActionId = npcActionId_
        self.npcMapId = npcMapId_
        
        super().__init__()
    
    
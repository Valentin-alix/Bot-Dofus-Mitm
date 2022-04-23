from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.NpcDialogCreationMessage import NpcDialogCreationMessage


class PortalDialogCreationMessage(NpcDialogCreationMessage):
    type:int
    

    def init(self, type_:int, mapId_:int, npcId_:int):
        self.type = type_
        
        super().__init__(mapId_, npcId_)
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildCharacsUpgradeRequestMessage(NetworkMessage):
    charaTypeTarget:int
    

    def init(self, charaTypeTarget_:int):
        self.charaTypeTarget = charaTypeTarget_
        
        super().__init__()
    
    
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatCommunityChannelCommunityMessage(NetworkMessage):
    communityId:int
    

    def init(self, communityId_:int):
        self.communityId = communityId_
        
        super().__init__()
    
    
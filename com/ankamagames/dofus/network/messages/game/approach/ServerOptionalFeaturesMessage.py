from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerOptionalFeaturesMessage(NetworkMessage):
    features:list[int]
    

    def init(self, features_:list[int]):
        self.features = features_
        
        super().__init__()
    
    
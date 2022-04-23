from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountHarnessColorsUpdateRequestMessage(NetworkMessage):
    useHarnessColors:bool
    

    def init(self, useHarnessColors_:bool):
        self.useHarnessColors = useHarnessColors_
        
        super().__init__()
    
    
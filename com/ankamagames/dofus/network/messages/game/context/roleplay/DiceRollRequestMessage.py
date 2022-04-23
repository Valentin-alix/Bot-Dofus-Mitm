from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DiceRollRequestMessage(NetworkMessage):
    dice:int
    faces:int
    channel:int
    

    def init(self, dice_:int, faces_:int, channel_:int):
        self.dice = dice_
        self.faces = faces_
        self.channel = channel_
        
        super().__init__()
    
    
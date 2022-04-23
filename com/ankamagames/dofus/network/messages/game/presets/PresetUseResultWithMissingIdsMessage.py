from com.ankamagames.dofus.network.messages.game.presets.PresetUseResultMessage import PresetUseResultMessage


class PresetUseResultWithMissingIdsMessage(PresetUseResultMessage):
    missingIds:list[int]
    

    def init(self, missingIds_:list[int], presetId_:int, code_:int):
        self.missingIds = missingIds_
        
        super().__init__(presetId_, code_)
    
    
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage


class CharacterFirstSelectionMessage(CharacterSelectionMessage):
    doTutorial:bool
    

    def init(self, doTutorial_:bool, id_:int):
        self.doTutorial = doTutorial_
        
        super().__init__(id_)
    
    
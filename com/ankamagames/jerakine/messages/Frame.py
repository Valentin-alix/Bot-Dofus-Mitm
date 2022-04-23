from com.ankamagames.jerakine.messages.MessageHandler import MessageHandler
from com.ankamagames.jerakine.utils.misc.Priotizable import Prioritizable


class Frame(MessageHandler, Prioritizable):
    def pushed(self) -> bool:
        pass

    def pulled(self) -> bool:
        pass

from whistle import EventDispatcher
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.messages.MessageHandler import MessageHandler


class IInteractive(EventDispatcher, IEntity):
    @property
    def handler(self) -> MessageHandler:
        pass

    @property
    def useHandCursor(self) -> bool:
        pass

    @property
    def enabledInteractions(self) -> int:
        pass
